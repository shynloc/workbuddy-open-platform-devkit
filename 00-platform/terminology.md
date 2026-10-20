---
title: WorkBuddy Open Platform Terminology
knowledge_type: DERIVED
official_sources:
  - workbuddy-open-platform-overview
  - workbuddy-skill
  - workbuddy-expert
  - workbuddy-expert-team
  - workbuddy-connector
  - workbuddy-buddy-app
  - workbuddy-third-party-app
last_verified: 2026-10-20
status: VERIFIED
---

# 核心术语

这份术语表用于帮助 Agent 快速判断产品边界。

| 术语 | 工程化理解 | 主要交付物 |
|---|---|---|
| Skill | 可复用方法/SOP/工作流 | SKILL.md + references/scripts/templates |
| Expert | 固定专业角色的人设+方法论 | plugin.json + agent MD + avatar |
| Expert Team | 多角色协作与主理人编排 | plugin.json + settings + 多 agents + avatars |
| Connector | 外部系统/账号/数据/操作能力接入 | connector-meta + MCP/CLI + icon + Skill |
| Buddy App | 垂直行业 AI Harness | 平台配置 + modes/scenes/market/connectors/models |
| Hardware Access | 智能眼镜、车机等硬件接入；第三方应用页当前两类 OAuth 应用之一 | 应用注册 + OAuth 2.1 + Open API |
| 积分兑换 | 用卡券或兑换码为用户兑换 credits；只开放积分与权益类 Scope | OAuth 应用 + `user.credit.exchange` |
| Share to WorkBuddy | 把文本、图片、音频、文件或资源链接预填到 WorkBuddy 任务输入区 | 分享应用 + 本地 RSA 签名，不是 client_secret |
| Third-party App | 上面三条的总称。Buddy 应用有自己的文档页，不再列在第三方应用类型表 | 按路径选择 OAuth 应用或分享应用 |
| Open API | WorkBuddy 对外能力接口 | OAuth、Local Assistant、Cloud Task、ACP、Artifacts、兑换码 |

## 组合关系

这些不是互斥产品。成熟方案通常组合使用：

```text
Buddy App
├── Experts / Expert Teams
├── Skills
├── Connectors
└── Third-party App / Open API integration (按需)
```