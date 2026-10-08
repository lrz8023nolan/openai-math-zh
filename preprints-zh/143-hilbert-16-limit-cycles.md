# Hilbert's Sixteenth Problem: Uniform Bounds for Limit Cycles
# 希尔伯特第十六问题：极限环的一致界

> **编号 143** ｜ 学科：动力系统与遍历理论 ｜ Lean 形式化：**有**（[lean/docs/143.md](https://github.com/openai/math/blob/main/lean/docs/143.md)）
> 本页对应本族全部 2 篇手稿 ｜ 基于上游 commit `adc7f12`（2026-10-06）｜ [成果族中文目录](../contents-zh/CONTENTS-zh.md)

---

## Manuscript 1 ｜ 手稿一：Uniform bounds for planar polynomial limit cycles

**Abstract（原文）**

> For every degree, we prove that the number of isolated periodic orbits of a real planar polynomial vector field is bounded by a finite constant depending only on that degree. This establishes the uniform boundedness assertion in the second part of Hilbert's sixteenth problem. The proof uses separation of asymptotic expansions on nested complex domains and a finite-dimensional counting argument.

**摘要（中译）**

> 对每个次数证明：实平面多项式向量场的孤立周期轨道个数由只依赖于该次数的有限常数界定。这建立了希尔伯特第十六问题第二部分的一致有界性断言。证明在嵌套复区域上使用渐近展开的分离与有限维计数论证。

**链接**：[uniform-bounds-for-planar-polynomial-limit-cycles.pdf](https://github.com/openai/math/blob/main/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf)

## Manuscript 2 ｜ 手稿二：Two limit cycles for quintic Liénard systems

**Abstract（原文）**

> Every classical Liénard system $`\dot x=y-F(x)`$, $`\dot y=-x`$, with <i>F</i> an arbitrary real polynomial of degree at most five, has at most two geometrically distinct isolated periodic orbits, and the bound is attained. This proves the degree-five case of the Lins Neto–de Melo–Pugh conjecture.

**摘要（中译）**

> 每个经典 Liénard 系统 $`\dot x=y-F(x)`$、$`\dot y=-x`$（<i>F</i> 为次数至多 5 的任意实多项式）至多有 2 个几何上不同的孤立周期轨道，且界可达。这证明 Lins Neto–de Melo–Pugh 猜想的五次情形。

**链接**：[two-limit-cycles-for-quintic-lienard-systems.pdf](https://github.com/openai/math/blob/main/preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/two-limit-cycles-for-quintic-lienard-systems-September-24-2026.pdf)

## Main result ｜ 主结果（成果族陈述）

**Original.**

> Resolves the uniform boundedness assertion in Hilbert's sixteenth problem: the number of isolated periodic orbits of a real planar polynomial vector field is bounded by a finite constant depending only on its degree. For classical quintic Liénard systems, the exact maximum is two limit cycles.

**中译。**

> 解决希尔伯特第十六问题第二部分的一致有界性断言：实平面多项式向量场的孤立周期轨道（极限环）个数由一个只依赖于次数的有限常数界定。对经典五次 Liénard 系统，精确最大值为 **2** 个极限环。

## Background ｜ 背景与意义（编者注）

希尔伯特第十六问题（1900）的第二部分问：次数为 <i>d</i> 的实平面多项式向量场最多能有多少个极限环（孤立的闭轨线）？这是常微分方程定性理论的核心悬案。即使 <i>d</i> = 2（二次系统），极限环个数的精确上界至今仍未完全确定；对一般 <i>d</i> ≥ 2，是否随次数一致有界（ $`H(d)\lt\infty`$）一百二十余年来毫无头绪——人们甚至能造出含十几个极限环的低次系统。

若第一篇手稿成立，则 $`H(d)\lt\infty`$ 对所有次数成立——这是整个问题的「存在性」突破；第二篇对经典的 Liénard 族给出精确值 2，与 Lins Neto–de Melo–Pugh 关于 Liénard 系统极限环个数的猜想（次数 $`2k+1`$ 至多 <i>k</i> 个极限环）在 <i>k</i> = 2 处一致。

本族附带 Lean 形式化。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
