# 翻译进度与认领状态

> 「摘要精译」指 summaries-zh/ 下的标准论文式对照翻译（标题／摘要／主结果中英对照 + 背景注解）；「全文翻译」指与上游 preprints/ 目录一一对应的完整论文中文版（LaTeX 复刻）；「成果族目录」指 contents-zh/CONTENTS-zh.md 的 372 族中文目录。

## 目录结构说明

`preprints-zh/` 目录结构与上游 `preprints/` 保持一致：

- **`preprints-zh/<手稿 Slug>/`**：与上游 `preprints/<手稿 Slug>/` 同名对应。内部 `build/` 为中文 LaTeX 译稿（`main-zh.tex` + `sections/` 等，对应上游的 `main.tex`），根目录 `paper-zh.pdf` 为编译产物（对应上游 `paper.pdf`）。
- **`preprints-zh/summaries-zh/`**：成果族级摘要精译（上游无对应层级，为本项目新增）。

## 摘要精译（summaries-zh/，按成果族编号排序）

| # | 成果族 | 学科 | Lean | 状态 | 译文 |
|---|---|---|---|---|---|
| 002 | 完整 BSD 公式（低 Selmer 余秩） | 数论 | ❌ | ✅ 完成 | [002-bsd-low-selmer-corank.md](preprints-zh/summaries-zh/002-bsd-low-selmer-corank.md) |
| 003 | 准黎曼猜想 | 数论 | ✅ | ✅ 完成 | [003-quasi-riemann-hypothesis.md](preprints-zh/summaries-zh/003-quasi-riemann-hypothesis.md) |
| 004 | ℚ 上的希尔伯特第十问题 | 数论 | ❌ | ✅ 完成 | [004-hilbert-tenth-q.md](preprints-zh/summaries-zh/004-hilbert-tenth-q.md) |
| 017 | π 的无理性指数为 2 | 数论 | ✅ | ✅ 完成 | [017-irrationality-exponent-pi.md](preprints-zh/summaries-zh/017-irrationality-exponent-pi.md) |
| 032 | CM 阿贝尔簇 Hodge 猜想与 K3 | 代数与复几何 | ❌ | ✅ 完成 | [032-cm-hodge-k3.md](preprints-zh/summaries-zh/032-cm-hodge-k3.md) |
| 074 | 挂谷问题（三维/四维） | 实与复分析 | ❌ | ✅ 完成 | [074-kakeya-3d-4d.md](preprints-zh/summaries-zh/074-kakeya-3d-4d.md) |
| 102 | 唯一游戏猜想 | 理论计算机科学 | ✅ | ✅ 完成 | [102-unique-games.md](preprints-zh/summaries-zh/102-unique-games.md) |
| 143 | 希尔伯特第十六问题：极限环一致界 | 动力系统与遍历理论 | ✅ | ✅ 完成 | [143-hilbert-16-limit-cycles.md](preprints-zh/summaries-zh/143-hilbert-16-limit-cycles.md) |
| 246 | Cannon 猜想 | 群论 | ✅ | ✅ 完成 | [246-cannon-conjecture.md](preprints-zh/summaries-zh/246-cannon-conjecture.md) |
| 287 | 自由群因子同构 | 算子代数 | ✅ | ✅ 完成 | [287-free-group-factors.md](preprints-zh/summaries-zh/287-free-group-factors.md) |

## 全文翻译（LaTeX 原版复刻）

用 XeLaTeX + ctexart 翻译上游 .tex 源码并重编译，章节、公式编号、定理环境与英文原文一一镜像；目录结构与上游一一对应（见上）。

| # | 手稿（Slug） | 所属成果族 | 状态 | 译稿 / PDF |
|---|---|---|---|---|
| 102-1 | [The-Unique-Games-Theorem-September-23-2026](https://github.com/openai/math/blob/main/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf)（唯一游戏定理） | 102 唯一游戏猜想 | ✅ 完成（59 页） | [build/](preprints-zh/The-Unique-Games-Theorem-September-23-2026/build/) ｜ [paper-zh.pdf](preprints-zh/The-Unique-Games-Theorem-September-23-2026/paper-zh.pdf) |
| 102-2 | [A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026](https://github.com/openai/math/blob/main/preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/paper.pdf)（最优 Max-Cut 难度的直接证明） | 102 唯一游戏猜想 | ✅ 完成（37 页） | [build/](preprints-zh/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/build/) ｜ [paper-zh.pdf](preprints-zh/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/paper-zh.pdf) |
| — | 其余 8 篇精选 | — | ⏳ 待译 | 逐篇推进，流程同上 |

## 成果族目录翻译（contents-zh/）

- 状态：**✅ 完成**——[CONTENTS-zh.md](contents-zh/CONTENTS-zh.md) 覆盖全部 **372 个成果族 / 722 篇手稿**（235 个族带 Lean 形式化标记），编号与上游一一对应，按 17 个学科分组。
- 后续深化：各手稿摘要的中文翻译与逐节精读，通过 issue 认领（见 CONTRIBUTING.md，待建）。

## 上游同步

- 本翻译基于上游 commit `adc7f12`（2026-10-06）。
- 上游承诺持续补充 Lean 形式化与修订。上游更新后，本表将标记过时译文。
