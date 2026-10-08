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

## v0.4 — Source Intelligence ✅

- [x] Source Watch 支持 visible-text hash + 章节 Heading Fingerprint
- [x] 自动映射 upstream source → 受影响 KB / Schema / Template / Validator
- [x] Source change 时生成 Review Artifact（JSON + Markdown）
- [x] 页面变化后自动生成 STALE 候选清单
- [x] 增加官方中文 / 英文文档技术关键项一致性检查
- [x] 官方模板 ZIP 变化时生成关键配置文件 diff
- [x] 官方页面与模板均坚持“检测 → Review → 更新”，不自动覆盖本地 KB

> 语义层面的最终判断仍由人/Agent Review 完成；WB-OPDK 不使用无人审核的自动同步替代官方规范判断。

## v0.5 — HTML Knowledge Base

- [x] 稳定 MkDocs 构建链路
- [ ] 决定是否启用 GitHub Pages
- [x] 加入来源 / knowledge_type / last_verified 可视化 Badge
- [x] 优化搜索与 Agent / Developer Quick Start 导航
- [x] 为 Templates / Schemas / Validators 生成 DevKit Tools 可视化入口
- [x] 加入官方来源 Freshness Dashboard

> HTML 知识库当前已经由 CI 构建并作为 artifact 输出。GitHub Pages 是额外公开部署入口，暂不自动开启。

## Working-grade Baseline ✅

内容与工程层已经达到可用于真实开发工作的基线：

- [x] 主体/服务类目/资质 Gate
- [x] Hardware 一等接入路径
- [x] Security & Governance
- [x] Post-release Operations
- [x] NOTICE / Compatibility / Security Policy
- [x] Source Registry + Impact Map Validator
- [x] Repository Doctor
- [x] Skill / Expert / Expert Team 已取得真实 Platform Parse 证据
- [x] Skill / Expert / Expert Team 均已通过平台审核并正式发布

质量定义见：

`QUALITY_GATES.md`

这不等于 v1.0 Runtime-complete；Connector、Buddy App、Open API 等真实验证仍按下述 Gate 继续推进。

## v1.0 — Production-ready DevKit

真实平台验证 Gate 见：

`95-validation/v1-readiness.md`

目标：

- 主要开放平台能力均有 OFFICIAL 规范页
- 每一类资产有 Starter Template
- 每一类可打包资产有 Validator
- 有统一 Runtime Test / Security / Submission QA
- 官方来源变更可检测
- HTML 知识库稳定构建
- 至少用真实 Skill、Expert、Expert Team、Connector、Buddy App 各验证一次