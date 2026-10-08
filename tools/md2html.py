# -*- coding: utf-8 -*-
"""preprints-zh/*.md -> HTML（KaTeX 公式），供 Edge 打印为 PDF。"""
import glob, io, re, os, markdown, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # openai-math-zh/
SRC = os.path.join(ROOT, 'preprints-zh')
OUT = os.path.join(ROOT, 'tools', 'pdf_build')
os.makedirs(OUT, exist_ok=True)

TPL = """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>__TITLE__</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body,{delimiters:[{left:'\\\\(',right:'\\\\)',display:false},{left:'$$',right:'$$',display:true}]});"></script>
<style>
@page { size: A4; margin: 21mm 19mm 19mm 19mm; }
html { -webkit-print-color-adjust: exact; }
body { font-family: "Times New Roman", "SimSun", serif; font-size: 10.8pt;
       line-height: 1.72; color: #1a1a1a; max-width: 170mm; margin: 0 auto; }
h1 { font-size: 16.5pt; text-align: center; line-height: 1.5;
     margin: 0.2em 0 0.15em; font-weight: bold; }
h1 + h1 { font-size: 13.5pt; color: #333; margin-bottom: 0.6em; }
h2 { font-size: 12.5pt; border-bottom: 1.2pt solid #444; padding-bottom: 2pt;
     margin: 1.4em 0 0.5em; }
h3 { font-size: 11.2pt; margin: 1.1em 0 0.35em; }
blockquote { border-left: 2.5pt solid #9a9a9a; background: #f7f7f5;
             margin: 0.45em 0; padding: 0.35em 0.9em; }
blockquote p { margin: 0.25em 0; }
p { margin: 0.5em 0; text-align: justify; }
hr { border: none; border-top: 0.6pt solid #bbb; margin: 1.2em 0; }
table { border-collapse: collapse; margin: 0.6em auto; font-size: 10pt; }
th, td { border: 0.6pt solid #888; padding: 3pt 7pt; }
th { background: #efefec; }
code { font-family: Consolas, "Courier New", monospace; font-size: 0.88em;
       background: #f2f2ef; padding: 0 3pt; }
pre { background: #f4f4f1; border: 0.5pt solid #ccc; padding: 7pt 10pt;
      overflow-x: hidden; }
pre code { background: none; }
.katex { font-size: 1.02em; }
</style></head><body>
__BODY__
</body></html>"""

def convert(path):
    text = io.open(path, encoding='utf-8-sig').read()
    store = []
    def keep(m):
        store.append(m.group(1))
        return f'MATHPLACE{len(store)-1}X'
    # 展示型数学块 ```math ... ```  -> $$..$$
    def keep_block(m):
        store.append('$$' + m.group(1).strip() + '$$')
        return f'MATHPLACE{len(store)-1}X'
    text = re.sub(r'```math\s*\n(.*?)```', keep_block, text, flags=re.S)
    # 行内 $`...`$ -> \(..\)
    text = re.sub(r'\$`(.+?)`\$', keep, text, flags=re.S)
    html = markdown.markdown(text, extensions=['tables'])
    def put(m):
        i = int(m.group(1))
        s = store[i]
        if s.startswith('$$'):
            return s
        return r'\(' + s + r'\)'
    html = re.sub(r'MATHPLACE(\d+)X', put, html)
    # 占位符若落在 <p> 内，公式还原为原始文本即可
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.S)
    title = re.sub(r'<[^>]+>', '', m.group(1)) if m else os.path.basename(path)
    return TPL.replace('__TITLE__', title).replace('__BODY__', html)

for md in sorted(glob.glob(os.path.join(SRC, '*.md'))):
    name = os.path.splitext(os.path.basename(md))[0]
    out = os.path.join(OUT, name + '.html')
    io.open(out, 'w', encoding='utf-8').write(convert(md))
    print('html:', name)
print('done ->', OUT)
