# 287 · 自由群因子的同构

> 学科：算子代数 ｜ Lean 形式化：**有** ｜ 译文基于上游 commit `adc7f12`（2026-10-06）

## 结果陈述

解决自由群因子同构问题：$`L(\mathbb F_2)\cong L(\mathbb F_3)`$，从而所有插值自由群因子（包括 $`L(\mathbb F_\infty)`$）彼此同构。它们共同的因子基本群为 $`\mathbb R_{\gt 0}`$。

## 手稿摘要（中译）

1. **[An isomorphism of the free group factors](https://github.com/openai/math/blob/main/preprints/An-isomorphism-of-the-free-group-factors-September-23-2026/An-isomorphism-of-the-free-group-factors-September-23-2026.pdf)**
   证明 $`L(\mathbb F_2)`$ 与 $`L(\mathbb F_3)`$ 作为迹 von Neumann 代数同构，正面解决自由群因子同构问题。由经典的自由群因子二择一原理，所有插值自由群因子（含 $`L(\mathbb F_\infty)`$）彼此同构，且基本群为 $`\mathbb R_{\gt 0}`$。

## 背景与意义（编者注）

von Neumann 代数是「无限维矩阵代数」的抽象；因子是其中结构最基本的一类，按迹类型分类（II₁ 型等）。1930 年代 Murray–von Neumann 构造了由自由群 $`\mathbb F_n`$ 的左正则表示生成的 II₁ 因子 $`L(\mathbb F_n)`$，并发现对 <i>n</i> ≥ 2 它们不再能用当时的量区分——这些「自由群因子」彼此是否同构，成为算子代数领域近百年悬而未决的头号问题。1980 年代 Voiculescu 创立自由概率论，算出了一批新的不变量（自由熵等），仍未判定 <i>n</i> = 2 与 3 是否同构；Dykema 与 Rădulescu 进一步证明插值自由群因子只可能有一个或可数多个同构类（二择一），使「$`L(\mathbb F_2)\cong L(\mathbb F_3)`$」成为唯一待决的关键点。

若本手稿成立，则所有插值自由群因子合并为一类，且其基本群为 $`\mathbb R_{\gt 0}`$（与已知构造一致）。本族附带 Lean 形式化（见上游 `lean/docs/287.md`）。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
