---
title: WorkBuddy Open API Capability Map
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-openapi
last_verified: 2026-10-07
status: VERIFIED
---

# Open API 能力地图

官方当前按以下能力域组织接口：

- 认证授权 API
- 个人资料 API
- 本地助理 API
- 云端任务 API
- ACP 通道
- 会话产物
- 兑换码核销 API

接入前需要开发者账号、已创建的第三方应用，以及相应 clientId/clientSecret。

## Third-party App 已公开 Scope（当前文档）

- `user.profile.readable`
- `user.contact.readable`
- `user.credit.exchange`
- `user.task.invokable`
- `user.task.readable`
- `user.localassistant.invokable`
- `user.localassistant.readable`

实际申请时以应用管理页面当前可选 Scope 为准，坚持最小权限。
