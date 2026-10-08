# 143 · 希尔伯特第十六问题：极限环的一致界

> 学科：动力系统与遍历理论 ｜ Lean 形式化：**有** ｜ 译文基于上游 commit `adc7f12`（2026-10-06）

## 结果陈述

解决希尔伯特第十六问题第二部分的一致有界性断言：实平面多项式向量场的孤立周期轨道（极限环）个数由一个只依赖于次数的有限常数界定。对经典五次 Liénard 系统，精确最大值为 **2** 个极限环。

## 各手稿摘要（中译）

1. **[Uniform bounds for planar polynomial limit cycles](https://github.com/openai/math/blob/main/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf)**
   对每个次数证明：实平面多项式向量场的孤立周期轨道个数由只依赖于该次数的有限常数界定。这建立了希尔伯特第十六问题第二部分的一致有界性断言。证明在嵌套复区域上使用渐近展开的分离与有限维计数论证。

2. **[Two limit cycles for quintic Liénard systems](https://github.com/openai/math/blob/main/preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/two-limit-cycles-for-quintic-lienard-systems-September-24-2026.pdf)**
   每个经典 Liénard 系统 $`\dot x=y-F(x)`$、$`\dot y=-x`$（<i>F</i> 为次数至多 5 的任意实多项式）至多有 2 个几何上不同的孤立周期轨道，且界可达。这证明 Lins Neto–de Melo–Pugh 猜想的五次情形。

## 背景与意义（编者注）

希尔伯特第十六问题（1900）的第二部分问：次数为 <i>d</i> 的实平面多项式向量场最多能有多少个极限环（孤立的闭轨线）？这是常微分方程定性理论的核心悬案。即使 <i>d</i> = 2（二次系统），极限环个数的精确上界至今仍未完全确定；对一般 <i>d</i> ≥ 2，是否随次数一致有界（ $`H(d)\lt\infty`$）一百二十余年来毫无头绪——人们甚至能造出含十几个极限环的低次系统。

若第一篇手稿成立，则 $`H(d)\lt\infty`$ 对所有次数成立——这是整个问题的「存在性」突破；第二篇对经典的 Liénard 族 $`\dot x = y - F(x),\ \dot y = -x`$（<i>F</i> 次数 ≤ 5）给出精确值 2，与 Lins Neto–de Melo–Pugh 关于 Liénard 系统极限环个数的猜想（次数 $`2k+1`$ 至多 <i>k</i> 个极限环）在 <i>k</i> = 2 处一致。

本族附带 Lean 形式化（见上游 `lean/docs/143.md`）。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
