import re, json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1) 学科映射：overview.tex \cataloguesection{Subject}{n} 与 \resultentry{num}...
tex = open('upstream/math/overview.tex', encoding='utf-8').read()
subjects = {}
cur_subj = None
for line in tex.splitlines():
    ms = re.match(r'\\cataloguesection\{(.+?)\}\{\d+\}', line.strip())
    if ms: cur_subj = ms.group(1); continue
    me = re.match(r'\\resultentry\{(\d+)\}', line.strip())
    if me and cur_subj: subjects[me.group(1)] = cur_subj
print("subjects found:", len(set(subjects.values())), "| entries mapped:", len(subjects))
for s in sorted(set(subjects.values())): print(" -", s, len([1 for v in subjects.values() if v==s]))

# 2) 修补解析：给 families 加 subject；补齐漏掉的手稿（无摘要型）
families = json.load(open('tools/contents_parsed.json', encoding='utf-8'))
src = open('upstream/math/CONTENTS.md', encoding='utf-8').read()

for f in families:
    f['subject'] = subjects.get(f['num'], '未分类')

# 找出未捕获的 &emsp; 链接（按链接路径判断）
captured = {m['link'] for f in families for m in f['manuscripts']}
all_links = re.findall(r'&emsp;\[([^\]]+)\]\(([^)]+)\)', src)
missing = [(t,l) for t,l in all_links if l not in captured]
print("missing manuscripts:", len(missing))
for t,l in missing: print("  *", t[:70], "->", l[:80])

# 兜底：无摘要或格式变体 —— 附加到其所在的 family（按链接中的 preprints 目录名匹配 family 手稿相邻性太难，
# 简化：这些一般是 family 的第一篇或独立块，这里只记录到 tools/missing_manuscripts.json 供人工核对）
json.dump(missing, open('tools/missing_manuscripts.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(families, open('tools/contents_parsed.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
n_man = sum(len(f['manuscripts']) for f in families)
print("families:", len(families), "| captured manuscripts:", n_man)
