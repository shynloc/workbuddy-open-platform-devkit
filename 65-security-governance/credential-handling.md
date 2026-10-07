---
title: Credential Handling
knowledge_type: DERIVED
official_sources:
  - workbuddy-third-party-app
  - workbuddy-openapi
last_verified: 2026-10-08
status: VERIFIED
---

# Credential Handling

## client_secret

官方明确：

- 应用创建后只完整展示一次；
- 不得暴露在前端或客户端代码中。

因此：

- 仅服务端 Secret Store；
- 不进 Git；
- 不写镜像层；
- 不写客户端/硬件固件；
- 日志自动脱敏。

## access_token

- 使用服务端响应的 `expires_in`，不要写死 TTL；
- 不进入 URL query；
- 不出现在错误日志；
- 传输只走 TLS。

## refresh_token

官方第三方应用页当前描述为长期刷新凭据，并要求安全保存在服务端。

工程上：

- 加密静态存储；
- 与用户/应用绑定；
- 轮换时覆盖旧值；
- 授权撤销/解绑时删除；
- 不下发设备端。

## MCP / Connector Token

用户自填 Token：

- 由 WorkBuddy 本地配置/注入；
- schema 中敏感字段使用 password；
- Connector 包内只放 `${VAR}` 占位符。

## Incident

凭据疑似泄露：

```text
Revoke/Rotate
→ invalidate sessions
→ inspect logs
→ notify affected owner
→ patch root cause
→ post-incident record
```
