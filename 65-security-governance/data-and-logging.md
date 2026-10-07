---
title: User Data and Logging
knowledge_type: DERIVED
official_sources:
  - workbuddy-third-party-app
last_verified: 2026-10-08
status: VERIFIED
---

# User Data & Logging

## Data minimization

只读取完成当前功能必需的数据。

不要因为 API 可以返回更多字段就全部保存。

## Suggested data inventory

每个集成都应记录：

- data source
- fields read
- fields written
- purpose
- retention
- storage location
- encryption
- deletion trigger

## Logging

日志优先记录：

- request id
- endpoint/tool name
- status
- latency
- error class
- account/internal subject pseudonym

默认不记录：

- access/refresh token
- client_secret
- Authorization header
- OAuth code
- ACP ticket
- 用户完整私密正文
- 未脱敏文件内容

## Retention

保留期限应由业务必要性驱动，不以“以后可能有用”为理由无限保留。

用户解除绑定/删除账户时，应定义关联数据如何删除或匿名化。
