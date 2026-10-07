---
title: WorkBuddy Open API Quick Reference
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-openapi
last_verified: 2026-10-07
status: VERIFIED
---

# Open API 快速参考

> 这里只做工程索引，不替代官方接口文档。请求/响应字段在真正接入时必须回查官方当前页面。

## OAuth

- GET `https://www.workbuddy.cn/openapi/v2/authorize`
- POST `https://www.workbuddy.cn/openapi/v2/token`

授权码一次性使用；应用服务端使用 client_id / client_secret 换取 token。使用 `state` 防 CSRF，redirect_uri 必须与登记值一致。

## Local Assistant

- GET `/openapi/v2/localassistant` — 在线状态 — `user.localassistant.readable`
- POST `/openapi/v2/localassistant/message` — 发送消息 — `user.localassistant.invokable`
- GET `/openapi/v2/localassistant/message` — 消息历史/增量轮询 — `user.localassistant.readable`

历史接口支持 `limit` / `offset`，也可传 `message_id` 获取该消息之后的新消息。

## Cloud Tasks

- POST `/openapi/v2/tasks` — 创建任务 — `user.task.invokable`
- GET `/openapi/v2/tasks` — 任务列表 — `user.task.readable`
- GET `/openapi/v2/tasks/{task_id}` — 查询任务并刷新 ACP link/token — `user.task.readable`

任务状态当前文档包含：CREATING、idle、planning、working、pending、completed、failed、archived、deleted。

## ACP

创建/查询任务返回 link + token 后：

1. GET `{link}` 建 SSE 接收通道，带 Bearer token；
2. 从响应头读取 `Acp-Connection-Id`；
3. POST `{link}` 发送 JSON-RPC，并带相同连接 ID；
4. 建连后依次 initialize → session/load → session/prompt。

ACP token 遇到 401 时，通过 GET `/tasks/{task_id}` 获取新 token，不要假设固定有效期。

## 其他能力

当前官方 Open API 还包含：

- User/Profile/Contact
- Session Artifacts
- Redemption Code / Credits

具体 endpoint 与 scope 以官方当前接口页为准。
