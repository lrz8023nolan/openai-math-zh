# Kakeya Maximal Conjecture in Three Dimensions / Full Hausdorff Dimension in Four
# 挂谷问题：三维极大算子猜想与四维满维数

> **编号 074** ｜ 学科：实与复分析 ｜ Lean 形式化：**无**
> 本页对应本族全部 2 篇手稿 ｜ 基于上游 commit `adc7f12`（2026-10-06）｜ [成果族中文目录](../contents-zh/CONTENTS-zh.md)

---

## Manuscript 1 ｜ 手稿一：The Kakeya maximal conjecture in three dimensions

**Abstract（原文）**

> We prove the Kakeya maximal conjecture in three dimensions. For every <i>ε</i> &gt; 0, the maximal average over unit tubes of radius <i>δ</i> maps $`L^3(\mathbb R^3)`$ to $`L^3(S^2)`$ with norm at most $`C_\varepsilon\delta^{-\varepsilon}`$.

**摘要（中译）**

> 证明三维挂谷极大算子猜想：对每个 <i>ε</i> &gt; 0，单位方向上半径 <i>δ</i> 细管的极大平均算子把 $`L^3(\mathbb R^3)`$ 映到 $`L^3(S^2)`$，范数至多 $`C_\varepsilon\delta^{-\varepsilon}`$。

**链接**：[paper.pdf](https://github.com/openai/math/blob/main/preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/paper.pdf)

## Manuscript 2 ｜ 手稿二：Every four-dimensional Kakeya set has full Hausdorff dimension

**Abstract（原文）**

> We prove the four-dimensional Hausdorff-dimension Kakeya conjecture: every subset of ℝ⁴ containing a unit line segment in every direction has Hausdorff dimension four. No compactness or regularity assumption is imposed on the set or its witnessing line family.

**摘要（中译）**

> 证明四维豪斯多夫维数形式的挂谷猜想：ℝ⁴ 中每个在每个方向都含单位线段的子集豪斯多夫维数为 4。对集合及其见证线族不施加任何紧性或正则性假设。

**链接**：[paper.pdf](https://github.com/openai/math/blob/main/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/paper.pdf)

## Main result ｜ 主结果（成果族陈述）

**Original.**

> Resolves the Kakeya maximal conjecture in three dimensions and the Hausdorff-dimension conjecture in four. In three dimensions, the radius-<i>δ</i> tube maximal operator maps $`L^3(\mathbb R^3)`$ to $`L^3(S^2)`$ with norm $`O_\varepsilon(\delta^{-\varepsilon})`$ for every <i>ε</i> &gt; 0. In four dimensions, every set containing a unit segment in every direction has Hausdorff dimension four.

**中译。**

> 解决三维挂谷极大算子猜想与四维豪斯多夫维数猜想。三维情形：半径 <i>δ</i> 细管的极大平均算子对每个 <i>ε</i> &gt; 0 以范数 $`O_\varepsilon(\delta^{-\varepsilon})`$ 把 $`L^3(\mathbb R^3)`$ 映到 $`L^3(S^2)`$。四维情形：每个在所有方向上都含一个单位线段的集合，其豪斯多夫维数为 4（即满维数）。

## Background ｜ 背景与意义（编者注）

挂谷集合是在**每个方向**都包含一段单位线段的集合，问题问这种集合「最瘦」能有多小。挂谷集合维数猜想（1917 年问题起源，Besicovitch 构造其测度可为零）断言：每个 <i>n</i> 维挂谷集合的豪斯多夫维数都是 <i>n</i>。该猜想是调和分析的中心问题——傅里叶限制理论、Bochner–Riesz 求和、波动方程局部光滑等重要估计都与它等价或受它支配。

历史脉络（供对照）：三维集合的豪斯多夫维数此前最佳下界为 5/2（Wolff），近年 Wang–Zahl（2025）宣布解决三维挂谷**集合**维数猜想；但本族针对的**极大算子** $`L^3`$ 估计是更强、应用更直接的命题，四维豪斯多夫维数此前也远未达到满维数。若两篇手稿成立，则三维极大算子猜想与四维集合维数猜想同时解决。

注意：本族**无** Lean 形式化，结果目前只是「声称」。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
