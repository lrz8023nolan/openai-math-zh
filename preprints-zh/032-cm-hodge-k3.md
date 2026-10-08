# 032 · 复 CM 阿贝尔簇的有理 Hodge 猜想与 K3 曲面

> 学科：代数与复几何 ｜ Lean 形式化：**无** ｜ 译文基于上游 commit `adc7f12`（2026-10-06）

## 结果陈述

对每个复 CM（复乘）阿贝尔簇，在**每个维数与余维数**下证明有理 Hodge 猜想。经由 Milne 的定理，这同时给出有限域上所有阿贝尔簇的 Tate 猜想，以及每种特征下阿贝尔簇的 Hodge 标准猜想。配套结果对射影复 K3 曲面的任意乘积证明有理 Hodge 猜想，并证明每个此类曲面的 Kuga–Satake 对应的代数性。

## 主要手稿摘要（中译，全族共 8 篇，此处为 4 篇核心；其余见上游目录）

1. **[The rational Hodge conjecture for CM abelian varieties](https://github.com/openai/math/blob/main/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-September-30-2026/paper.pdf)**
   证明具有复乘的复阿贝尔簇的有理 Hodge 猜想：此类簇上的每个有理 Hodge 类都是有理代数闭链类的线性组合。作为推论得到 CM 阿贝尔簇的广义 Hodge 猜想、有限域上阿贝尔簇的 Tate 猜想，以及任意特征下阿贝尔簇的 Hodge 标准猜想。

2. **[The rational Hodge conjecture for products of K3 surfaces](https://github.com/openai/math/blob/main/preprints/The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026/hodge-conjecture-products-k3.pdf)**
   证明每个射影复 K3 曲面有限乘积的有理 Hodge 猜想：每个有理 Hodge 类都是代数的。因子可以不同或重复，对其 Picard 数、周期或自同态域无任何限制。

3. **[Algebraicity of Kuga–Satake Correspondences for K3 Surfaces](https://github.com/openai/math/blob/main/preprints/Algebraicity-of-Kuga-Satake-Correspondences-for-K3-Surfaces-October-3-2026/manuscript.pdf)**
   证明每个光滑射影复 K3 曲面的 Kuga–Satake 对应都是代数的：其超越上同调到 Kuga–Satake 阿贝尔簇上同调的指定嵌入由一个有理代数闭链诱导（固定正规化与完整偶 Clifford 靶）。结论对带迁移嵌入的同源 Kuga–Satake 模型同样成立。

4. **[Weil classes and Hodge classes on abelian powers](https://github.com/openai/math/blob/main/preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-September-30-2026/paper.pdf)**
   对具有虚二次作用与相容极化（有理同调 Hermite 型符号 $`(3,3)`$ 双曲）的复阿贝尔六重簇的每个自乘幂，在每个余维数证明有理 Hodge 猜想；对维数至多 5、可虚二次作用的复阿贝尔簇同样成立。

## 背景与意义（编者注）

Hodge 猜想是千禧年大奖难题之一：断言复代数簇上每个（有理系数）Hodge 类都是代数闭链类的有理线性组合。阿贝尔簇是其最重要的试验场；CM 阿贝尔簇（自同态环足够大的一类）因结构刚性而成为最有希望突破的情形。K3 曲面与阿贝尔簇的联系由 Kuga–Satake 构造建立——把 K3 的超越上同调嵌入某个阿贝尔簇的上同调——因此「Kuga–Satake 对应是否代数」长期以来是把 K3 的 Hodge 猜想归约到阿贝尔簇的关键悬案。若本族成立，则：CM 阿贝尔簇情形完全解决；射影 K3 曲面的任意乘积情形解决；Kuga–Satake 对应对每个射影复 K3 曲面都是代数的。这些都是数十年的核心问题。

注意：本族**无** Lean 形式化，结果目前只是「声称」。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。全族 8 篇手稿清单见 [上游 CONTENTS](https://github.com/openai/math/blob/main/CONTENTS.md)。
