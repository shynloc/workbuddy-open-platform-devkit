---
title: Connector Authentication and Credentials
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-connector
last_verified: 2026-10-07
status: VERIFIED
---

# Connector 认证与凭据

## 模式

### 标准 MCP OAuth / 无认证

`auth_mode` 可省略，按标准 MCP 流程连接。

### WorkBuddy 托管 OAuth

`server-side` 或 `gateway`，官方要求接入前与 WorkBuddy 团队确认。

### 用户自填 Token

使用：

```json
"auth_mode": "token"
```

并提供 `token-schema.json`。最低 WorkBuddy 版本不低于 4.23.0。

凭据保存在用户本机并在连接时注入，不经过云端；不会打开浏览器。

### CLI 登录

由 cli.json 的 auth/status/unAuth 管理。

## MCP OAuth

WorkBuddy 内置 OAuth 管理器按 OAuth 2.1 + PKCE 工作，客户端不持有 client_secret。服务端需提供：

- protected resource metadata
- authorization server metadata
- 动态客户端注册
- authorize
- token

官方要求 PKCE S256；授权码一次性使用；redirect_uri 精确匹配；支持 WorkBuddy 私有协议回调，并在必要时允许 loopback 回退。

## token-schema

核心字段：

- title
- description
- docUrl/docLabel（可选）
- fields[]

字段项：

- key
- label
- type=text/password
- required
- placeholder
- defaultValue
- description

敏感字段必须 password。多语言使用 `_en` 平行字段。

同一服务如果既提供 OAuth 又提供 Token，官方要求使用两个不同 source，作为两个独立连接器。
