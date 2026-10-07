---
title: WorkBuddy OAuth 2.1
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-openapi
  - workbuddy-third-party-app
last_verified: 2026-10-07
status: VERIFIED
---

# OAuth 2.1

## 授权码流程

授权页：

```text
GET https://www.workbuddy.cn/openapi/v2/authorize
```

官方当前参数：

- response_type=code
- client_id
- redirect_uri（必须在应用登记集合中）
- scope（空格分隔；不传则为完整授权列表）
- state（官方建议，用于 CSRF 防护与状态保持）

收到 code 后由应用服务端换取访问凭证。

## 安全基线

- client_secret 只在后端使用
- redirect_uri 与开放平台登记保持一致
- state 使用不可预测随机值
- 最小权限申请 Scope
- refresh_token 服务端安全保存
- 前端不得持有长期敏感凭据
