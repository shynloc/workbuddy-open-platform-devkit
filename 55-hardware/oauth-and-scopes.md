---
title: Hardware OAuth and Scopes
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-third-party-app
  - workbuddy-openapi
last_verified: 2026-10-08
status: VERIFIED
---

# Hardware OAuth & Scopes

硬件接入应用通过 OAuth 2.1 获取用户授权。

官方流程：

```text
Create Hardware App
→ Configure Scopes
→ Configure OAuth Redirect URI
→ Submit Review
→ Approved / Enabled
→ User Authorizes
→ Backend Exchanges Code
→ Call Open API
```

当前公开 Scope 包括：

- `user.profile.readable`
- `user.contact.readable`
- `user.credit.exchange`
- `user.task.invokable`
- `user.task.readable`
- `user.localassistant.invokable`
- `user.localassistant.readable`

硬件应用官方说明可按业务需要申请全部权限，但仍必须遵循最小权限原则。

## Hardware-specific rule

不要因为“硬件应用可申请全部权限”就默认全选。

例如只做语音触发 PC Agent：

- 可能只需要 localassistant readable/invokable；
- 不应顺带申请任务、积分或用户联系方式权限。

最终以开放平台当前应用权限页面可选 Scope 为准。
