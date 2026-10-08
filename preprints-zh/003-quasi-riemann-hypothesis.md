# 003 · 准黎曼猜想

> 学科：数论 ｜ Lean 形式化：**有** ｜ 译文基于上游 commit `adc7f12`（2026-10-06）

## 结果陈述

证明每个狄利克雷 <i>L</i> 函数（包括黎曼 ζ 函数）在半平面 $`\Re s\gt 7/8`$ 内无零点，解决准黎曼猜想。对 $`\mathbb Q(\sqrt{-3})`$ 上每个有限阶 Hecke <i>L</i> 函数，同一半平面也无零点。配套论文给出 $`\Re s\gt 11/12`$ 无零点半平面的另一证明。

## 各手稿摘要（中译）

1. **[The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)**
   证明 $`\mathbb Q(\sqrt{-3})`$ 上所有有限阶 Hecke <i>L</i> 函数与所有狄利克雷 <i>L</i> 函数在半平面 $`\Re s\gt 7/8`$ 内无零点（允许 <i>s</i> = 1 处的主极点）。特别地，黎曼 ζ 函数在该半平面无零点，即准黎曼猜想成立。

2. **[The Quasi-Riemann Hypothesis (alternate 11/12 proof)](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf)**
   通过证明每个狄利克雷 <i>L</i> 函数（含 ζ 函数）在 $`\Re s\gt 11/12`$ 内无零点建立准黎曼猜想；对 $`K=\mathbb Q(\sqrt{-3})`$ 上每个有限阶 Hecke <i>L</i> 函数同样成立。特别地，这排除了 Landau–Siegel 零点的存在。

3. **[Uniform exclusion of Landau–Siegel zeros](https://github.com/openai/math/blob/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf)**
   证明 Landau–Siegel 零点的一致排除：存在绝对常数 <i>c</i> &gt; 0，使得导体 <i>q</i> ≥ 3 的每个本原非主实狄利克雷 <i>L</i> 函数的每个实零点 $`\beta\in(0,1)`$ 满足 $`(1-\beta)\log q\ge c`$。

## 背景与意义（编者注）

黎曼猜想（1859）断言 ζ 函数的全部非平凡零点落在实部为 1/2 的竖线上，至今未决。百余年来的经典方法（de la Vallée Poussin、Vinogradov–Korobov 型零点自由区域）得到的无零点区域都会随虚部增大而越来越贴近实部为 1 的直线，始终无法「撑」出一条**固定宽度**的无零点竖直带。准黎曼猜想正是退而求其次的目标：找到某个固定常数 $`\theta\lt 1`$，使 $`\Re s\gt \theta`$ 的整个半平面无零点。

若本结果成立，其意义包括：素数分布误差项的实质改进；Landau–Siegel 零点不存在（这是类域论中类数歧义等问题的核心障碍）。注意 $`\theta=7/8`$ 距离完整的黎曼猜想（$`\theta=1/2`$）仍有本质距离。

本族附带 Lean 形式化（见上游 `lean/docs/003.md`），即证明已由计算机逐行检查。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
