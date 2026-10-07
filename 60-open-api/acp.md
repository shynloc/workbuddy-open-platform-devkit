---
title: ACP Channel
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-openapi
last_verified: 2026-10-08
status: VERIFIED
---

# ACP 通道

官方来源：https://open.workbuddy.cn/docs/openapi

ACP（Agent Client Protocol）用于和云端任务会话建立实时双向通信。

## 连接信息

先通过“创建云端任务”或“查询云端任务”获取：

- link
- token / task_ticket
- expire_at

## 通信模型

官方当前描述：

- SSE 长连接：接收流式回答和通知
- POST：发送 JSON-RPC 2.0 调用
- GET/POST 双通道通过同一个连接标识关联

## 生命周期

```text
Create/Query Task
→ get link + task_ticket
→ open SSE
→ POST JSON-RPC
→ consume stream/events
→ ticket expires
→ Query Task 获取新 ticket
→ reconnect
```

## 工程建议

- 实现断线重连；
- 不把 task_ticket 写进客户端持久日志；
- 收到 401 时先重新查询任务换取票据；
- 处理重复事件/网络重放；
- ACP 和 REST artifacts 应组合使用，而不是二选一。
