---
title: token-schema.json Reference
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-connector
last_verified: 2026-10-08
status: VERIFIED
---

# token-schema.json

适用于 `auth_mode: "token"`，最低 WorkBuddy 版本 4.23.0。

## 目的

定义用户在 WorkBuddy 中填写长期凭据的表单。凭据保存在用户本机并在连接时注入，不应打包在连接器中。

## 常见字段

顶层：

- title
- description
- docUrl（可选）
- docLabel（可选）
- fields[]

field：

- key
- label
- type: text | password
- required
- placeholder
- defaultValue
- description

多语言使用对应 `_en` 字段。

## 约束

- 敏感字段使用 password；
- key 必须与 mcp.json 中的 `${VAR_NAME}` 精确匹配；
- 不把真实默认 Secret 写入 defaultValue；
- 描述里告诉用户凭据去哪里获取；
- 如果服务同时提供 OAuth 与 Token，官方要求使用不同 source、作为两个独立 Connector。
