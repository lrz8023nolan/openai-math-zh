# openai/math 中文对照版

> **非官方中文阅读版** —— 本项目是 [openai/math](https://github.com/openai/math) 的中文对照翻译，与英文原文逐篇对应阅读。翻译不构成对原文结果的验证或背书。

## 这是什么

2026 年 10 月 6 日，OpenAI 在 GitHub 上公开了由其内部模型产出的 **722 篇数学手稿**（归入 **372 个成果族**），覆盖数论、几何、理论计算机科学等 17 个学科方向，部分成果附有 Lean 形式化证明。

本仓库将其中文目录、总览与精选译文开源，供中文读者对照阅读。

## ⚠️ 使用前必读

1. **原文结果处于不同验证阶段。** 约六成成果族附有 [Lean 形式化](https://github.com/openai/math/tree/main/lean)（计算机逐行检查过的证明），**其余结果仅为「声称」，可能存在错误**。OpenAI 官方已明确说明这一点。本目录逐篇保留验证状态标注。
2. **译文以英文原文为准。** 译文为 AI 辅助翻译 + 人工校对，术语以 [glossary.md](glossary.md) 为准。译文与原文有任何冲突，一律以英文原文为准。
3. **这不是同行评审出版物。** 上游手稿未经学术同行评审，引用时请注明其性质。

## 目录

| 内容 | 说明 |
|---|---|
| [contents-zh/CONTENTS-zh.md](contents-zh/CONTENTS-zh.md) | 372 个成果族的中文目录（编号与上游一一对应，含 Lean 形式化标记） |
| [glossary.md](glossary.md) | 数学术语中英对照表（翻译基准） |
| [overview-zh/](overview-zh/) | 上游 overview（研究总览）中文版 |
| [preprints-zh/](preprints-zh/) | 精选手稿中文版——目录结构与上游 `preprints/` 一一对应：`<手稿 Slug>/build/` 内为 LaTeX 中文译稿，`<手稿 Slug>/paper-zh.pdf` 为编译 PDF；[summaries-zh/](preprints-zh/summaries-zh/) 为成果族摘要精译 |
| [progress.md](progress.md) | 翻译进度与认领状态 |

## 与上游的对应关系

- 本翻译基于上游 commit `adc7f12`（2026-10-06）。上游更新后，我们会在 progress.md 标记过时译文。
- 每篇手稿的 PDF、LaTeX 源码与 Lean 形式化请直接访问[上游仓库](https://github.com/openai/math)，本仓库不复制原始文件。

## 参与翻译

见 [CONTRIBUTING.md](CONTRIBUTING.md)。翻译前请先阅读术语表；认领通过 issue 进行。

## 许可证与致谢

- 原始作品 © [OpenAI](https://github.com/openai/math)，以 [Apache License 2.0](LICENSE) 授权。
- 中文翻译作为衍生作品同样以 Apache License 2.0 分发，详见 [NOTICE.md](NOTICE.md)。
