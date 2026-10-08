# 004 · ℚ 上的希尔伯特第十问题

> 学科：数论 ｜ Lean 形式化：**无** ｜ 译文基于上游 commit `adc7f12`（2026-10-06）

## 结果陈述

证明不存在算法判定「任意多个变量的整系数多项式是否有有理零点」，从而对 ℚ 上的希尔伯特第十问题给出否定解答（变量个数属于输入的一部分）。

## 各手稿摘要（中译）

1. **[Hilbert's tenth problem over the rational numbers](https://github.com/openai/math/blob/main/preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/main.pdf)**
   对 ℚ 上的希尔伯特第十问题给出否定解答：没有算法判定整系数多项式是否有有理零点。变量个数属于输入。

2. **[A pointwise 2-converse for elliptic curves with rational two-torsion](https://github.com/openai/math/blob/main/preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/paper.pdf)**
   对 ℚ 上具有非零有理 2-挠的椭圆曲线证明逐点的 2-逆定理：若 $`2^\infty`$-Selmer 余秩为 0 或 1，则解析秩与 Mordell–Weil 秩都等于该余秩，且 Shafarevich–Tate 群有限。结果允许在 2 处任意约化。

## 背景与意义（编者注）

希尔伯特第十问题（1900 年提出）问：是否存在算法判定任意丢番图方程是否有（整数）解。1970 年 Matiyasevich（结合 Davis–Putnam–Robinson）证明：对**整数**解，这样的算法不存在——问题在 ℤ 上已解决。但把「整数」换成「有理数」（ℚ）后，问题重新打开，成为算术几何最著名的未决问题之一：ℚ 上丢番图集的结构远比 ℤ 上难以刻画，已知技术（椭圆曲线秩的 Selmer 界、域的丢番图定义等）只给出大量部分结果。

若本手稿成立，则 ℚ 上的希尔伯特第十问题与 ℤ 上同样以否定告终——「有理数解的存在性」本质上是不可判定的。同族第二篇（椭圆曲线 2-逆定理）是配套的算术几何工具性结果。

注意：本族**无** Lean 形式化，结果目前只是「声称」。

---

> ⚠️ 原文结果未经同行评审。译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](../glossary.md) 为准；译文与英文原文冲突时以英文原文为准。
