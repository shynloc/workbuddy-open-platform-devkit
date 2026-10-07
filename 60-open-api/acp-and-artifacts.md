---
title: WorkBuddy ACP and Session Artifacts
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-openapi
last_verified: 2026-10-07
status: VERIFIED
---

# ACP 与会话产物

## ACP 建连

Cloud Task 创建/查询得到 `link` 与 `token` 后：

1. `GET {link}`，带 `Authorization: Bearer {token}` 与 `Accept: text/event-stream`；
2. 从响应头读取 `Acp-Connection-Id`；
3. `POST {link}` 发送 JSON-RPC，请求头带同一个连接 ID；
4. 建连后标准流程：`initialize → session/load → session/prompt`。

官方说明 ACP 使用 SSE 接收 + POST 发送的双通道模式。

如果 ACP 请求返回 401，通过 `GET /openapi/v2/tasks/{task_id}` 获取新 token。

## 消息类型

SSE 主要包含：

- Notification（无 id）：流式回答、状态变化等
- Server-to-Client Request（有 id）：需要客户端应答，如工具授权、AskUserQuestion
- session/prompt Response：一轮 prompt 的权威结束信号

## WorkBuddy 私有扩展

官方当前定义：

```text
_codebuddy.ai/artifact
```

用于 plan / tasks / media / overview 等产物的增量推送。

event：

- created
- updated
- deleted

客户端应使用 `artifact.uri` 作为主键执行 upsert/delete。

## 产物 REST

```text
GET {sandbox_url}/api/session/artifacts
Authorization: Bearer {task_ticket}
```

查询参数：

- sessionId
- type = plan | tasks | media | overview
- startMs
- endMs
- limit（1–500；0/省略表示不分页）
- offset

推荐恢复策略：

```text
首屏 REST 拉全量
→ artifact.uri 建索引
→ SSE _codebuddy.ai/artifact 增量更新
```

两路数据同源，按 uri 覆盖即可保持幂等。
