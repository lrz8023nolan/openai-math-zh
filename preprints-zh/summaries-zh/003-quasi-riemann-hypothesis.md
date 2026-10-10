# The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8
# 准黎曼猜想：Re s > 7/8 的无零点半平面

> **编号 003** ｜ 学科：数论 ｜ Lean 形式化：**有**（[lean/docs/003.md](https://github.com/openai/math/blob/main/lean/docs/003.md)）
> 本页对应本族全部 3 篇手稿 ｜ 基于上游 commit `adc7f12`（2026-10-06）｜ [成果族中文目录](../contents-zh/CONTENTS-zh.md)

---

## Abstract ｜ 摘要

**Abstract（原文）**

> We prove that all finite-order Hecke <i>L</i>-functions over $`\mathbb Q(\sqrt{-3})`$ and all Dirichlet <i>L</i>-functions are zero-free in the half-plane $`\Re s\gt 7/8`$, with the principal pole at <i>s</i> = 1 allowed. In particular, the Riemann zeta function is zero-free in this half-plane, proving the quasi-Riemann hypothesis.

**摘要（中译）**

> 证明 $`\mathbb Q(\sqrt{-3})`$ 上所有有限阶 Hecke <i>L</i> 函数与所有狄利克雷 <i>L</i> 函数在半平面 $`\Re s\gt 7/8`$ 内无零点（允许 <i>s</i> = 1 处的主极点）。特别地，黎曼 ζ 函数在该半平面无零点，即准黎曼猜想成立。

**链接**：[paper.pdf](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)

## Main result ｜ 主结果（成果族陈述）

**Original.**

> Proves that every Dirichlet <i>L</i>-function, including $`\zeta(s)`$, is zero-free in $`\Re s\gt 7/8`$, resolving the quasi-Riemann hypothesis. The same half-plane is zero-free for every finite-order Hecke <i>L</i>-function over $`\mathbb Q(\sqrt{-3})`$. A companion gives a different proof of the zero-free half-plane $`\Re s\gt 11/12`$.

**中译。**

> 证明每个狄利克雷 <i>L</i> 函数（包括 $`\zeta(s)`$）在 $`\Re s\gt 7/8`$ 内无零点，解决准黎曼猜想。对 $`\mathbb Q(\sqrt{-3})`$ 上每个有限阶 Hecke <i>L</i> 函数，同一半平面也无零点。配套论文给出 $`\Re s\gt 11/12`$ 无零点半平面的另一证明。

## Other manuscripts ｜ 本族其他手稿

### 2. The Quasi-Riemann Hypothesis (alternate 11/12 proof)

**Abstract（原文）**

> We establish the quasi-Riemann hypothesis by proving that every Dirichlet <i>L</i>-function, including Riemann's zeta function, has no zeros in the half-plane $`\mathop{\mathrm{Re}}\nolimits s\gt 11/12`$. More generally, we prove the same zero-free half-plane for every finite-order Hecke <i>L</i>-function over $`K=\mathbb Q(\sqrt{-3})`$. In particular, this rules out the existence of Landau–Siegel zeros.

**摘要（中译）**

> 通过证明每个狄利克雷 <i>L</i> 函数（含 ζ 函数）在 $`\Re s\gt 11/12`$ 内无零点建立准黎曼猜想；对 $`K=\mathbb Q(\sqrt{-3})`$ 上每个有限阶 Hecke <i>L</i> 函数同样成立。特别地，这排除了 Landau–Siegel 零点的存在。

**链接**：[paper2.pdf](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf)

### 3. Uniform exclusion of Landau–Siegel zeros

**Abstract（原文）**

> We prove the uniform exclusion of Landau–Siegel zeros. There is an absolute constant <i>c</i> &gt; 0 such that every real zero $`\beta\in(0,1)`$ of every primitive nonprincipal real Dirichlet <i>L</i>-function of conductor <i>q</i> ≥ 3 satisfies $`(1-\beta)\log q\ge c`$.

**摘要（中译）**

> 证明 Landau–Siegel 零点的一致排除：存在绝对常数 <i>c</i> &gt; 0，使得导体 <i>q</i> ≥ 3 的每个本原非主实狄利克雷 <i>L</i> 函数的每个实零点 $`\beta\in(0,1)`$ 满足 $`(1-\beta)\log q\ge c`$。

**链接**：[paper.pdf](https://github.com/openai/math/blob/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf)

## Background ｜ 背景与意义（编者注）

黎曼猜想（1859）断言 ζ 函数的全部非平凡零点落在实部为 1/2 的竖线上，至今未决。百余年来的经典方法（de la Vallée Poussin、Vinogradov–Korobov 型零点自由区域）得到的无零点区域都会随虚部增大而越来越贴近实部为 1 的直线，始终无法「撑」出一条**固定宽度**的无零点竖直带。准黎曼猜想正是退而求其次的目标：找到某个固定常数 $`\theta\lt 1`$，使 $`\Re s\gt \theta`$ 的整个半平面无零点。

若本结果成立，其意义包括：素数分布误差项的实质改进；Landau–Siegel 零点不存在（这是类域论中类数歧义等问题的核心障碍）。注意 $`\theta=7/8`$ 距离完整的黎曼猜想（$`\theta=1/2`$）仍有本质距离。

本族附带 Lean 形式化，即证明已由计算机逐行检查。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
