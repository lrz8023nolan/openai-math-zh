# 102 · 唯一游戏猜想与最优近似阈值

> 学科：理论计算机科学 ｜ Lean 形式化：**有** ｜ 译文基于上游 commit `adc7f12`（2026-10-06）

## 结果陈述

证明 Khot 的唯一游戏猜想（Unique Games Conjecture, 2002）。独立的直接归约还在**无权图**上建立：Max-Cut 超过 Goemans–Williamson 比值的近似是 NP 难的；顶点覆盖低于因子 2 的近似是 NP 难的；Min-UnCut 与有向反馈点集的任意固定常数因子近似是 NP 难的。这些直接证明使用已有的 PCP 与 Label Cover 难度结果。

## 各手稿摘要（中译）

1. **[The Unique Games Theorem](https://github.com/openai/math/blob/main/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf)**
   证明唯一游戏猜想：对每个固定的 $`\varepsilon,\delta\in(0,1/2)`$，给出从 3SAT 到固定有限字母表上唯一游戏的确定性多项式时间归约，完备性至少 $`1-\varepsilon`$、可靠性至多 <i>δ</i>。

2. **[A Direct Proof of Optimal Max-Cut Hardness](https://github.com/openai/math/blob/main/preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/paper.pdf)**
   证明在简单无权图上，把 Max-Cut 近似到任何优于 Goemans–Williamson 常数的固定因子都是 NP 难的。

3. **[The Factor-Two Hardness Threshold for Vertex Cover](https://github.com/openai/math/blob/main/preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/paper.pdf)**
   证明最小顶点覆盖在简单无权图上难以近似到任何低于 2 的固定因子。

4. **[Constant-factor hardness of Min-UnCut](https://github.com/openai/math/blob/main/preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/paper.pdf)**
   对每个固定 <i>C</i> &gt; 1，Min-UnCut 的 <i>C</i> 因子近似在简单无向无权图上是 NP 难的。

5. **[Constant-factor hardness of directed feedback vertex set](https://github.com/openai/math/blob/main/preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/paper.pdf)**
   最小有向反馈点集的任意固定常数因子近似在无权有向图上是 NP 难的。

## 背景与意义（编者注）

唯一游戏猜想是 Khot 于 2002 年提出的一个关于「唯一标记约束系统」的难度假设：断言存在一类近似判定问题，区分「几乎全部约束可满足」与「几乎全部不可满足」是 NP 难的。它悬置了二十余年，是近似算法领域的分水岭：若为真，则 Max-Cut 的 Goemans–Williamson 0.878 比值、顶点覆盖的 2 近似等一批经典算法是**最优的**（条件NP 难度）；若为假，则一批近似算法可被改进。本族若成立，这些「条件性最优」全部变成无条件 NP 难度，且独特游戏假设本身成为定理。

本族附带 Lean 形式化（见上游 `lean/docs/102.md`）。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
