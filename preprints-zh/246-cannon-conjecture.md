# Cannon's Conjecture
# Cannon 猜想

> **编号 246** ｜ 学科：群论 ｜ Lean 形式化：**有**（[lean/docs/246.md](https://github.com/openai/math/blob/main/lean/docs/246.md)）
> 本页对应本族全部 1 篇手稿 ｜ 基于上游 commit `adc7f12`（2026-10-06）｜ [成果族中文目录](../contents-zh/CONTENTS-zh.md)

---

## Abstract ｜ 摘要

**Abstract（原文）**

> We prove that every hyperbolic group whose boundary is homeomorphic to the two-sphere admits a proper cocompact isometric action on hyperbolic three-space with finite kernel. This resolves Cannon's conjecture positively.

**摘要（中译）**

> 证明边界同胚于二维球面的每个双曲群都容许一个核对数有限、在双曲三维空间上正常余紧的等距作用，正面解决 Cannon 猜想。

**链接**：[paper.pdf](https://github.com/openai/math/blob/main/preprints/A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026/paper.pdf)

## Main result ｜ 主结果（成果族陈述）

**Original.**

> Every word-hyperbolic group with boundary homeomorphic to <i>S</i>² admits a proper cocompact isometric action on hyperbolic three-space with finite kernel, proving Cannon's conjecture. Every torsion-free such group is therefore the fundamental group of a closed hyperbolic three-manifold.

**中译。**

> 每个边界同胚于 <i>S</i>² 的词双曲群，都允许一个核对数有限、在双曲三维空间上正常余紧的等距作用，从而证明 Cannon 猜想。每个无挠的此类群因此是某个闭双曲三维流形的基本群。

## Background ｜ 背景与意义（编者注）

Cannon 猜想（1994 前后）断言：若词双曲群 <i>G</i> 的理想边界 $`\partial G`$ 同胚于二维球面 $`S^2`$，则 <i>G</i> 与双曲三维空间等距群 $`\mathrm{Isom}(\mathbb H^3)`$ 的格（离散余紧子群）基本等价。它是几何群论中最著名的「双曲化」问题之一：三维情形的特殊性来自双曲三维流形理论（Perelman 的几何化定理此前只把**流形群**双曲化，而 Cannon 猜想面对的是抽象给定的双曲群——群本身可以是病态的，甚至可能无挠性或有限表现性以外的任何额外结构）。

已知的部分结果（小消去群、曲率化方法、Special 群等）只覆盖特殊类。若本手稿成立，则结合无挠性立得：每个无挠、边界为 $`S^2`$ 的双曲群是闭双曲三维流形的基本群——即三维双曲群论中「抽象到几何」的最后一环。

本族附带 Lean 形式化。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
