# An Isomorphism of the Free Group Factors
# 自由群因子的同构

> **编号 287** ｜ 学科：算子代数 ｜ Lean 形式化：**有**（[lean/docs/287.md](https://github.com/openai/math/blob/main/lean/docs/287.md)）
> 本页对应本族全部 1 篇手稿 ｜ 基于上游 commit `adc7f12`（2026-10-06）｜ [成果族中文目录](../contents-zh/CONTENTS-zh.md)

---

## Abstract ｜ 摘要

**Abstract（原文）**

> We solve the free group factor isomorphism problem affirmatively by proving that $`L(\mathbb F_2)`$ and $`L(\mathbb F_3)`$ are isomorphic as tracial von Neumann algebras. The classical free group factor alternative then implies that all interpolated free group factors, including $`L(\mathbb F_\infty)`$, are isomorphic and have fundamental group $`\mathbb R_{\gt 0}`$.

**摘要（中译）**

> 证明 $`L(\mathbb F_2)`$ 与 $`L(\mathbb F_3)`$ 作为迹 von Neumann 代数同构，正面解决自由群因子同构问题。由经典的自由群因子二择一原理，所有插值自由群因子（含 $`L(\mathbb F_\infty)`$）彼此同构，且基本群为 $`\mathbb R_{\gt 0}`$。

**链接**：[An-isomorphism-of-the-free-group-factors.pdf](https://github.com/openai/math/blob/main/preprints/An-isomorphism-of-the-free-group-factors-September-23-2026/An-isomorphism-of-the-free-group-factors-September-23-2026.pdf)

## Main result ｜ 主结果（成果族陈述）

**Original.**

> Resolves the free group factor isomorphism problem: $`L(\mathbb F_2)\cong L(\mathbb F_3)`$, and hence all interpolated free group factors, including $`L(\mathbb F_\infty)`$, are isomorphic. Their common factor has fundamental group $`\mathbb R_{\gt 0}`$.

**中译。**

> 解决自由群因子同构问题：$`L(\mathbb F_2)\cong L(\mathbb F_3)`$，从而所有插值自由群因子（包括 $`L(\mathbb F_\infty)`$）彼此同构。它们共同的因子基本群为 $`\mathbb R_{\gt 0}`$。

## Background ｜ 背景与意义（编者注）

von Neumann 代数是「无限维矩阵代数」的抽象；因子是其中结构最基本的一类，按迹类型分类（II₁ 型等）。1930 年代 Murray–von Neumann 构造了由自由群 $`\mathbb F_n`$ 的左正则表示生成的 II₁ 因子 $`L(\mathbb F_n)`$，并发现对 <i>n</i> ≥ 2 它们不再能用当时的量区分——这些「自由群因子」彼此是否同构，成为算子代数领域近百年悬而未决的头号问题。1980 年代 Voiculescu 创立自由概率论，算出了一批新的不变量（自由熵等），仍未判定 <i>n</i> = 2 与 3 是否同构；Dykema 与 Rădulescu 进一步证明插值自由群因子只可能有一个或可数多个同构类（二择一），使「$`L(\mathbb F_2)\cong L(\mathbb F_3)`$」成为唯一待决的关键点。

若本手稿成立，则所有插值自由群因子合并为一类，且其基本群为 $`\mathbb R_{\gt 0}`$（与已知构造一致）。

本族附带 Lean 形式化。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
