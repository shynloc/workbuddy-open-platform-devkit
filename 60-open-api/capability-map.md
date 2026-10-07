---
title: WorkBuddy Open API Capability Map
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-openapi
  - workbuddy-third-party-app
last_verified: 2026-10-07
status: VERIFIED
---

# Open API 能力地图

官方当前按以下能力域组织接口：

- 认证授权 API
- 用户资料 / 联系方式
- 本地助理 API
- 云端任务 API
- ACP 通道
- 会话产物
- 积分 / 兑换码核销 API

接入前需要开发者账号、已创建的第三方应用，以及相应 clientId/clientSecret。

## Third-party App 页面当前公开 Scope

- `user.profile.readable`
- `user.contact.readable`
- `user.credit.exchange`
- `user.task.invokable`
- `user.task.readable`
- `user.localassistant.invokable`
- `user.localassistant.readable`

## Open API Reference 额外出现的 Scope

当前英文 Open API Reference 的 `GET /openapi/v2/credit` 标注：

- `user.credit.readable`

但该 Scope 当前未出现在第三方应用页的公开 Scope 列表中。

因此不要静默假设它对所有应用类型可申请；实际申请以开放平台应用权限管理页为准。详见 `sources/known-inconsistencies.md`。

## 原则

实际申请时坚持最小权限，并以当前应用类型在开放平台实际可选 Scope 为准。
