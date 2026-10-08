import re, json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

src = open('upstream/math/CONTENTS.md', encoding='utf-8').read()

# family 头部：**NNN. Title.** description ...（可能含 [Lean](...)）
fam_re = re.compile(r'\*\*(\d{3})\.\s*(.+?)\.\*\*(.*?)(?=\n\n</td>)', re.S)
# 手稿：&emsp;[Title](link) \n\n abstract
man_re = re.compile(r'&emsp;\[([^\]]+)\]\(([^)]+)\)\s*\n\n(.*?)(?=\n\n</td>)', re.S)

# 按出现顺序切分文本块
blocks = re.split(r'<tbody><tr>\s*\n<td>\s*\n', src)
families = []
cur = None
for b in blocks:
    mfam = fam_re.search(b)
    if mfam:
        num, title, desc = mfam.group(1), mfam.group(2).strip(), mfam.group(3).strip()
        desc = re.sub(r'\s*\(\[Lean\]\(([^)]+)\)\)', lambda m: f' [LEAN:{m.group(1)}]', desc)
        cur = {'num': num, 'title': title, 'desc': desc, 'lean': 'LEAN:' in desc, 'manuscripts': []}
        families.append(cur)
    elif cur is not None:
        mman = man_re.search(b)
        if mman:
            cur['manuscripts'].append({'title': mman.group(1).strip(), 'link': mman.group(2), 'abstract': mman.group(3).strip()})

json.dump(families, open('tools/contents_parsed.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
n_man = sum(len(f['manuscripts']) for f in families)
n_lean = sum(1 for f in families if f['lean'])
print(f"families={len(families)} manuscripts={n_man} with_lean={n_lean}")
print("first:", families[0]['num'], families[0]['title'][:50])
print("last:", families[-1]['num'], families[-1]['title'][:50])
missing = [f['num'] for f in families if not f['manuscripts']]
print("families w/o manuscripts:", missing if missing else "none")
# 连续性检查
nums = [int(f['num']) for f in families]
gaps = [n for n in range(1, max(nums)+1) if n not in nums]
print("gaps:", gaps if gaps else "none")
