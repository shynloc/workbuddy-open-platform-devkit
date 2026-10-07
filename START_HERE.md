# START HERE — Agent Entry Point

> 本文件是 AI Agent 进入 WB-OPDK 时的首要入口。

## 0. Source of Truth

WB-OPDK 不是 WorkBuddy 官方文档替代品。

规则优先级：

1. WorkBuddy 当前官方开放平台文档
2. 官方开放平台实际 Schema / 后台行为
3. 本知识库中状态为 VERIFIED 的内容
4. OBSERVED 实测记录
5. DERIVED / EXPERIMENTAL 工程建议

当本地内容标记为 `STALE`、官方 source 发生变化、平台返回未知字段/校验错误、或用户反馈与知识库不一致时：**重新检查官方来源，不要猜。**

官方来源注册表：`sources/official-sources.yaml`

## 1. 先判断产品类型

读取：`00-platform/capability-decision-tree.md`

- 方法 / SOP → Skill
- 单一专业角色 → Expert
- 多角色真实协作 → Expert Team
- 外部 API / MCP / SaaS → Connector
- 垂直行业完整工作台 → Buddy App
- 外部 App / 网站 / 硬件调用 WorkBuddy → Third-party App / Open API

## 2. 再进入对应目录

- Skill → `10-skill/`
- Expert → `20-expert/`
- Expert Team → `30-expert-team/`
- Connector → `40-connector/`
- Buddy App → `50-buddy-app/`
- Open API → `60-open-api/`

## 3. 所有产品共用发布工程

开发中后期必须读取：`70-release-engineering/`

应覆盖：

需求 → 架构 → 开发 → QA → Runtime Test → 发布资料 → 打包 → 审核 → 返修 → 上线 → 版本维护

## 4. Agent 工作原则

- 不要一次性加载整个知识库。
- 优先读取当前产品类型 + 当前阶段需要的内容。
- 平台字段不得凭记忆杜撰。
- 官方文档未支持的能力，要明确说“未在当前官方来源中确认”。
- OBSERVED / DERIVED 内容不得包装为官方规定。
- 任何凭据、Token、Secret 都不得写入公开仓库。
