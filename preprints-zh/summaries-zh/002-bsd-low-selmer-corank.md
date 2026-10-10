# Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank
# 低 Selmer 余秩下的完整 BSD 公式

> **编号 002** ｜ 学科：数论 ｜ Lean 形式化：**无**（相关族 006 亦无）
> 本页对应本族全部 3 篇手稿 ｜ 基于上游 commit `adc7f12`（2026-10-06）｜ [成果族中文目录](../contents-zh/CONTENTS-zh.md)

---

## Manuscript 1 ｜ 手稿一：Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank

**Abstract（原文）**

> We prove the full Birch–Swinnerton-Dyer leading-term formula for every elliptic curve over ℚ whose full <i>q</i>-power Selmer group has corank zero or one at some prime <i>q</i>. The analytic and Mordell–Weil ranks equal that corank, and the Tate–Shafarevich group is finite. The formula includes all prime factors and requires no additional hypotheses on reduction, rational torsion, isogenies, complex multiplication, or residual Galois representations.

**摘要（中译）**

> 对 ℚ 上每条其完整 <i>q</i>-幂 Selmer 群在某素数 <i>q</i> 处余秩为 0 或 1 的椭圆曲线，证明完整 BSD 首项公式：解析秩与 Mordell–Weil 秩都等于该余秩，且 Tate–Shafarevich 群有限。公式包含全部素因子，且对约化、有理挠、同源、复乘或剩余伽罗瓦表示不附加任何额外假设。

**链接**：[exact-bsd-low-selmer-corank.pdf](https://github.com/openai/math/blob/main/preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/exact-bsd-low-selmer-corank.pdf)

## Manuscript 2 ｜ 手稿二：The Selmer converse for elliptic curves at every prime

**Abstract（原文）**

> We prove the Selmer converse in coranks zero and one for every elliptic curve over ℚ and every prime <i>p</i>: if the full <i>p</i>-power Selmer group has ℤ<sub><i>p</i></sub>-corank $`r\in\{0,1\}`$, then the analytic and Mordell–Weil ranks both equal <i>r</i>, and the entire Tate–Shafarevich group is finite. As an application at the additive prime 3, we prove that for every prime $`\ell\equiv4,7,8\pmod9`$, the cubic $`X^3+Y^3=\ell Z^3`$ has analytic and Mordell–Weil rank one and finite Tate–Shafarevich group. In particular, every such <i>ℓ</i> is a sum of two rational cubes.

**摘要（中译）**

> 对 ℚ 上每条椭圆曲线与每个素数 <i>p</i> 证明余秩 0 与 1 的 Selmer 逆定理：若完整 <i>p</i>-幂 Selmer 群的 $`\mathbb Z_p`$-余秩 $`r\in\{0,1\}`$，则解析秩与 Mordell–Weil 秩都等于 <i>r</i>，且整个 Tate–Shafarevich 群有限。作为加性素数 3 处的应用：对每个 $`\ell\equiv4,7,8\pmod9`$ 的素数，三次曲面 $`X^3+Y^3=\ell Z^3`$ 的解析秩与 Mordell–Weil 秩为 1、Tate–Shafarevich 群有限；特别地，每个这样的 <i>ℓ</i> 都是两个有理立方数之和。

**链接**：[main.pdf](https://github.com/openai/math/blob/main/preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026/main.pdf)

## Manuscript 3 ｜ 手稿三：The two-primary Birch–Swinnerton-Dyer formula in Selmer corank at most one

**Abstract（原文）**

> We prove the two-primary Birch and Swinnerton-Dyer leading-term formula for every elliptic curve over the rationals whose two-power Selmer group has corank at most one. In this range, the algebraic rank, analytic rank, and Selmer corank are equal, and the Tate–Shafarevich group is finite. Combined with the quadratic-twist Selmer distribution, this gives the exact two-primary formula for a density-one set of signed squarefree twists of each fixed curve, ordered by absolute value; the common rank is zero or one, with each value having density one half.

**摘要（中译）**

> 对 ℚ 上每条 2-幂 Selmer 群余秩至多 1 的椭圆曲线证明 2-主部 BSD 首项公式。在此范围内代数秩、解析秩与 Selmer 余秩相等，Tate–Shafarevich 群有限。结合二次扭曲的 Selmer 分布，对每条固定曲线按绝对值排序的带符号无平方因子扭曲中密度为一的集合给出精确的 2-主部公式；公共秩为 0 或 1，各占密度 1/2。

**链接**：[paper.pdf](https://github.com/openai/math/blob/main/preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026/paper.pdf)

## Main result ｜ 主结果（成果族陈述）

**Original.**

> Proves the full Birch–Swinnerton-Dyer leading-term formula for every elliptic curve over ℚ whose full <i>q</i>-power Selmer group has corank zero or one for some prime <i>q</i>, including finiteness of the Tate–Shafarevich group. With result 006, this gives full BSD for a density-one set of quadratic twists of every elliptic curve over ℚ.

**中译。**

> 对 ℚ 上每条椭圆曲线 <i>E</i>，只要其完整 <i>q</i>-幂 Selmer 群对某个素数 <i>q</i> 的余秩为 0 或 1，就证明完整的 Birch–Swinnerton-Dyer（BSD）首项公式，包括 Tate–Shafarevich 群的有限性。与成果 006 合起来，对 ℚ 上每条椭圆曲线的一个**密度为一**的二次扭曲集合给出完整 BSD 公式。

## Background ｜ 背景与意义（编者注）

BSD 猜想是千禧年大奖难题之一，把椭圆曲线的两个世界联系起来：代数侧的 Mordell–Weil 秩（有理点的「自由度」）与解析侧的 <i>L</i> 函数在 <i>s</i>=1 处的零点行为。完整猜想还要求 <i>L</i> 函数首项系数的精确公式（含 Tate–Shafarevich 群的阶）。

已知结果主要集中在解析秩 0/1 的情形（Gross–Zagier、Kolyvagin 一系工作，且需附加条件），以及函数域上的完整定理。本族声称的推进在于：以 Selmer 余秩为条件（而非解析秩），**不附加任何额外假设**地给出完整首项公式，包括全部素因子与 Sha 有限性；并与成果 006 的扭曲分布结合，把结论推到每条椭圆曲线的密度为一的二次扭曲集合。

注意：本族**无** Lean 形式化，结果目前只是「声称」。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
