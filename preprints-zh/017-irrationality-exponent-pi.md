# 017 · π 的无理性指数为 2

> 学科：数论 ｜ Lean 形式化：**有** ｜ 译文基于上游 commit `adc7f12`（2026-10-06）

## 结果陈述

证明 <i>π</i> 的无理性指数恰为 2：对每个 <i>ε</i> &gt; 0 与所有足够大的分母 <i>q</i>，每个有理数 $`p/q`$ 满足

```math
\left|\pi-\frac{p}{q}\right|\ \ge\ \frac{1}{q^{\,2+\varepsilon}} .
```

由此还证明经典 Flint–Hills 级数 $`\sum_{n\ge1}1/(n^3\sin^2 n)`$（角以弧度计）收敛。

## 手稿摘要（中译）

1. **[The irrationality exponent of pi is 2](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf)**
   证明 <i>π</i> 的无理性指数为 2 的猜想。作为推论，经典 Flint–Hills 级数 $`\sum_{n\ge1}1/(n^3\sin^2 n)`$（角以弧度计）收敛。

## 背景与意义（编者注）

实数 <i>α</i> 的**无理性指数** $`\mu(\alpha)`$ 是最大的 $`\mu`$，使不等式 $`| \alpha - p/q |\lt q^{-\mu}`$ 有无穷多组有理解 $`p/q`$。几乎所有实数的指数都是 2（Khinchin），<i>e</i> 的指数恰为 2（经典连分数理论）。但 <i>π</i> 的情形完全不同：由于缺少类似连分数的有效工具，<i>π</i> 的已知上界长期停留在 7.6 左右（Salikhov, 2008：$`\mu(\pi)\le 7.6063`$）——即「$`\pi`$ 不能被分母为 <i>q</i> 的有理数近似到 $`q^{-7.61}`$ 以内」，而猜想中的真值是 2。

本手稿声称一步跨到最优值 2：$`\pi`$ 的有理逼近不可能显著优于「无理性强迫」的 $`q^{-2-\varepsilon}`$ 速度。这同时解决 Flint–Hills 级数的收敛性——该级数在 1953 年提出后悬置七十余年，其收敛性恰被 $`\mu(\pi)\lt 5/2`$ 类型的界所控制。

本族附带 Lean 形式化（见上游 `lean/docs/017.md`）。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
