---
title: WorkBuddy Local Assistant API
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-openapi
last_verified: 2026-10-07
status: VERIFIED
---

# Local Assistant API

官方来源：https://open.workbuddy.cn/docs/openapi

本地助理 API 用于与用户 PC 端已连接的 WorkBuddy 本地助理交互。

## 查询在线状态

```text
GET /openapi/v2/localassistant
Scope: user.localassistant.readable
```

返回当前本地助理是否在线。

## 发送消息

```text
POST /openapi/v2/localassistant/message
Scope: user.localassistant.invokable
Content-Type: application/json
```

普通文本：

```json
{
  "content": "帮我查一下今天的日程",
  "msg_type": "text"
}
```

当前官方文档还描述 `permission_response`，用于回答 AskQuestion / 工具审批；其 `content` 仍为字符串，内部承载序列化 JSON。实现这类交互前必须回查官方当前字段。

## 查询消息历史

```text
GET /openapi/v2/localassistant/message
Scope: user.localassistant.readable
```

两种模式：

- 分页：`limit`（默认 20、上限 100）+ `offset`
- 增量：传 `message_id`，返回该消息之后的新消息

## 安全边界

Local Assistant 是对用户本地助理的远程触发入口。第三方应用不应绕过本地工具审批或用户确认机制；权限和消息类型必须以当前官方接口说明为准。
