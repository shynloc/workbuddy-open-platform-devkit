# START HERE — Agent Entry Point

> AI Agent 进入 WB-OPDK 时先读本文件。

## 0. Source of Truth

规则优先级：

1. WorkBuddy 当前官方开放平台文档
2. 官方开放平台实际 Schema / 后台行为
3. 本知识库 VERIFIED 内容
4. OBSERVED 实测
5. DERIVED / EXPERIMENTAL 工程建议

如果本地文档标记为 `STALE`、平台报未知字段/解析错误、或用户反馈与 KB 不一致：**先回查官方来源，不要猜。**

来源注册表：`sources/official-sources.yaml`  
治理规则：`sources/source-policy.md`

## 1. 判断产品类型

读取：`00-platform/capability-decision-tree.md`

- SOP / 方法 → Skill
- 固定专业角色 → Expert
- 多角色真实协作 → Expert Team
- 外部 API / MCP / CLI → Connector
- 垂直行业工作台 → Buddy App
- 外部 App / 网站 / 硬件调用 WorkBuddy → Third-party App / Open API

## 2. 按类型最小加载

### Skill

1. `10-skill/specification.md`
2. `10-skill/development-workflow.md`
3. `10-skill/qa-checklist.md`

### Expert

1. `20-expert/specification.md`
2. `20-expert/design-guide.md`
3. `20-expert/qa-checklist.md`

### Expert Team

1. `30-expert-team/specification.md`
2. `30-expert-team/orchestration.md`
3. 如需外部能力：`30-expert-team/dependencies.md`

### Connector

1. `40-connector/specification.md`
2. MCP → `40-connector/mcp-guide.md`
3. CLI → `40-connector/cli-guide.md`
4. 认证 → `40-connector/auth-and-credentials.md`
5. 新字段 → `40-connector/version-compatibility.md`
6. `40-connector/qa-checklist.md`

### Buddy App

1. `50-buddy-app/specification.md`
2. `50-buddy-app/product-design.md`
3. `50-buddy-app/configuration-and-release.md`
4. 视觉 → `50-buddy-app/design-assets.md`
5. B2B → `50-buddy-app/enterprise-distribution.md`

### Third-party App / Open API

1. `60-open-api/third-party-app.md`
2. `60-open-api/oauth-2.1.md`
3. `60-open-api/capability-map.md`

## 3. 所有类型共用 Release Engineering

开发中后期读取 `70-release-engineering/`：

需求 → 开发 → QA → Runtime Test → 发布资料 → 审核 → 版本维护

## 4. Agent 工作纪律

- 不一次性加载整个仓库；
- 字段不得凭记忆杜撰；
- OFFICIAL 与 DERIVED/OBSERVED 必须区分；
- 当前官方来源不支持的点要明确说“未确认”；
- 不把 Secret/Token/AppSecret 写进公开仓库；
- 有外部副作用的动作设计明确确认门槛；
- 发布前重新核验官方文档与当前开放平台界面。
