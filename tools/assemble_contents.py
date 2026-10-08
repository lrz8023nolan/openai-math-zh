# -*- coding: utf-8 -*-
import json, glob, io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

UP = 'https://github.com/openai/math/blob/main/'
fams_json = json.load(open('tools/contents_parsed.json', encoding='utf-8'))
by_num = {f['num']: f for f in fams_json}

SUBJ_ZH = {
 'Number theory':'数论','Algebraic and complex geometry':'代数与复几何',
 'Real and complex analysis':'实与复分析','Convex and metric geometry':'凸几何与度量几何',
 'Theoretical computer science':'理论计算机科学','Combinatorics':'组合数学',
 'Algebra':'代数','Group theory':'群论','Operator algebras':'算子代数',
 'Topology':'拓扑学','Functional analysis':'泛函分析','Differential geometry':'微分几何',
 'Partial differential equations':'偏微分方程','Mathematical physics':'数学物理',
 'Probability and statistical mechanics':'概率与统计力学',
 'Dynamical systems and ergodic theory':'动力系统与遍历理论','Mathematical logic':'数理逻辑',
}

# 读取全部 tsv 译文
zh = {}
for path in sorted(glob.glob('tools/zh/zh_*.tsv')):
    for line in open(path, encoding='utf-8-sig'):
        line = line.strip()
        if not line: continue
        parts = line.split('\t')
        if len(parts) != 4:
            print(f'BAD LINE in {path}: {line[:60]}'); sys.exit(1)
        num, title, desc, lean = parts
        zh[num] = (title, desc, lean == '1')

print('translated:', len(zh), '| expected: 372')
missing = [n for n in by_num if n not in zh]
extra   = [n for n in zh if n not in by_num]
print('missing:', missing if missing else 'none')
print('extra  :', extra if extra else 'none')
if missing or extra: sys.exit(1)

# 按学科分组（学科按其最小编号排序，近似上游顺序）
groups = {}
for num, f in by_num.items():
    groups.setdefault(f['subject'], []).append(num)

out = io.StringIO()
out.write('# 成果族中文目录（CONTENTS-zh）\n\n')
out.write('> **722 篇手稿，372 个成果族。** 编号与上游 [CONTENTS.md](https://github.com/openai/math/blob/main/CONTENTS.md) 一一对应，可对照阅读。\n')
out.write('> 手稿标题保留英文并链接至上游 PDF；「Lean」表示该族附有 [Lean 形式化](https://github.com/openai/math/tree/main/lean)。\n\n')
out.write('> ⚠️ 原文结果处于不同验证阶段，未经同行评审；译文以英文原文为准。基于上游 commit `adc7f12`（2026-10-06）。\n\n')

subjects_sorted = sorted(groups, key=lambda s: min(int(n) for n in groups[s]))
for si, subj in enumerate(subjects_sorted, 1):
    nums = sorted(groups[subj])
    out.write(f'## {si}. {SUBJ_ZH.get(subj, subj)}（{subj}，{len(nums)} 个族）\n\n')
    for num in nums:
        f = by_num[num]; title, desc, _ = zh[num]
        lean_txt = f'（[Lean 形式化]({UP}lean/docs/{num}.md)）' if f['lean'] else ''
        out.write(f'**{num}. {title}。** {desc}{lean_txt}\n\n')
        for m in f['manuscripts']:
            out.write(f'&emsp;[{m["title"]}]({UP}{m["link"]})\n\n')
    out.write('---\n\n')

open('contents-zh/CONTENTS-zh.md', 'w', encoding='utf-8').write(out.getvalue())
n_man = sum(len(by_num[n]['manuscripts']) for n in by_num)
print('written contents-zh/CONTENTS-zh.md |', len(by_num), 'families |', n_man, 'manuscripts |', sum(1 for f in by_num.values() if f['lean']), 'with Lean')
