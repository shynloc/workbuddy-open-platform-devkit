# ROADMAP

WB-OPDK 的目标不是复制官方文档，而是把 WorkBuddy 开放平台整理成可持续维护的工程开发底座。

## v0.3 — Schemas & Release Engineering ✅

- [x] 补全 Skill / Expert / Expert Team / Connector / Token 等字段级 DERIVED schema
- [x] 把官方 Expert / Expert Team 模板 ZIP 审计结果固化为 machine-readable report + baseline
- [x] 增加 Skill / Expert / Team / Connector Release Manifest
- [x] 增加 CLI Connector 完整 starter 与 Validator
- [x] 增加第三方应用 OAuth 最小可运行参考实现
- [x] 增加端到端“需求 → 发布包” Recipe
- [x] 增加一键 Release Check：Validator → Manifest → ZIP

## v0.4 — Source Intelligence

- [ ] 将 Source Watch 输出升级为结构化字段级/章节级 diff
- [ ] 自动映射 upstream source → 受影响 KB / Schema / Template / Validator
- [ ] Source change 时生成待处理 Issue 草稿或 Review Artifact
- [ ] 页面 hash 变化后辅助生成 STALE 候选清单
- [ ] 增加官方文档中文/英文版本一致性检查
- [ ] 官方模板 ZIP 变化时生成关键配置文件 diff

## v0.5 — HTML Knowledge Base

- [x] 稳定 MkDocs 构建链路
- [ ] 决定是否启用 GitHub Pages
- [ ] 加入来源 / knowledge_type / last_verified 可视化 Badge
- [ ] 优化搜索与“Agent / Developer Quick Start”导航
- [ ] 为 Templates / Schemas / Validators 生成可视化工具入口
- [ ] 加入当前官方来源 freshness dashboard

## v1.0 — Production-ready DevKit

目标：

- 主要开放平台能力均有 OFFICIAL 规范页
- 每一类资产有 Starter Template
- 每一类可打包资产有 Validator
- 有统一 Runtime Test / Security / Submission QA
- 官方来源变更可检测
- HTML 知识库稳定构建
- 至少用真实 Skill、Expert、Expert Team、Connector、Buddy App 各验证一次
