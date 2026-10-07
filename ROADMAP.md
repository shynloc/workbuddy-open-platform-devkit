# ROADMAP

WB-OPDK 的目标不是复制官方文档，而是把 WorkBuddy 开放平台整理成可持续维护的工程开发底座。

## v0.3 — Schemas & Release Engineering

- [ ] 继续补全 Expert / Expert Team / Connector 字段级 schema
- [ ] 把官方模板 ZIP 审计结果固化为 machine-readable report
- [ ] 增加 Skill / Expert / Team / Connector release manifest
- [ ] 增加 CLI Connector 更完整 starter
- [ ] 增加第三方应用 OAuth 最小参考实现
- [ ] 增加端到端“需求 → 发布包” Recipe

## v0.4 — Source Intelligence

- [ ] 将 source watch 输出转成结构化 diff
- [ ] 自动映射 upstream source → 受影响 KB 文件
- [ ] Source change 时自动生成待处理 Issue 草稿
- [ ] 页面 hash 变化后辅助标记 STALE
- [ ] 增加官方文档英文/中文版本一致性检查

## v0.5 — HTML Knowledge Base

- [ ] 稳定 MkDocs 导航
- [ ] 决定是否启用 GitHub Pages
- [ ] 加入来源/验证日期 Badge
- [ ] 加入搜索与“Agent 入口”快捷路径
- [ ] 为模板和 Validator 生成可视化入口

## v1.0 — Production-ready DevKit

目标：

- 主要开放平台能力均有 OFFICIAL 规范页
- 每一类资产有 Starter Template
- 每一类可打包资产有 Validator
- 有统一 Runtime Test / Security / Submission QA
- 官方来源变更可检测
- HTML 知识库稳定构建
- 至少用真实 Skill、Expert、Team、Connector、Buddy App 各验证一次
