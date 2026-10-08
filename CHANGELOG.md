# Changelog

## Unreleased — Working-grade Baseline

- 微信公众号文章全流程发布 v1.0.0 已通过 WorkBuddy 平台审核并正式发布，成为 WB-OPDK 首个完整 Skill 平台生命周期案例
- 补齐主体认证、个人/非个人服务类目与资质 Gate
- 增加 Hardware 接入架构、OAuth/Scope、Runtime 和设备安全
- 增加 Security & Governance：Trust Boundary、凭据、数据日志、Side-effect Policy、Release Gate
- 增加 Post-release Operations：监控、版本兼容、回滚、事故响应、弃用和支持交接
- 增加 NOTICE、Compatibility Policy、Security Policy、Quality Gates
- 增加 Source Registry / Impact Map Validator 和 Repository Doctor
- 将 Qualification 官方页面纳入 Source Watch baseline
- Expert 与 Expert Team 真实包均通过 WorkBuddy Platform Parse 并进入审核
- 真实 Team Parser 明确要求 plugin root 使用 settings.json；Starter / Validator 已修正


## 2026-10-08 — Tooling / v0.2

- 增加 Skill / Expert / Expert Team / Connector package validators
- 增加 release ZIP packer
- 增加官方来源 snapshot hash 脚本与 schema
- 完成 Expert Team starter 的 Lead / Research / Delivery Agent 模板
- 完成 MCP Connector starter：meta / mcp / token-schema / icon / Skill / README
- 扩充 Open API：Local Assistant / Cloud Task / ACP / Session Artifacts
- 增加 Runtime Test Plan 与 Security Checklist
- 增加 Third-party App Recipe
- 记录 Buddy App 工作模式数量、Expert Team setting/settings 等官方内部不一致
- 修复 Expert Team starter，不再同时保留 setting.json 与 settings.json

## 2026-10-07 — Foundation / v0.1

- 创建 WB-OPDK 公开仓库骨架
- 建立 Official-first Source Policy
- 登记 WorkBuddy 官方来源
- 完成 Skill / Expert / Expert Team 首版规范与 QA
- 完成 Connector 首版 MCP/CLI/Auth/Version Compatibility/QA
- 完成 Buddy App 产品、配置、设计资产、企业分发首版
- 完成 Third-party App / OAuth / Open API 能力地图首版
- 建立 Release Engineering、Recipes、Templates
- 增加官方来源 hash 检查脚本与 KB metadata validator