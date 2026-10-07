---
title: WorkBuddy Cloud Task API
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-openapi
last_verified: 2026-10-07
status: VERIFIED
---

# Cloud Task API

## 创建任务

```text
POST /openapi/v2/tasks
Scope: user.task.invokable
```

请求：

```json
{
  "prompt": "任务初始指令",
  "name": "可选任务名"
}
```

响应可包含：

- task_id
- status
- name
- link（ACP）
- token
- expire_at
- sandboxLink
- sandboxDataLink

创建后 link/token 可能暂时未就绪；官方建议可轮询单任务查询直到补齐。

## 查询任务列表

```text
GET /openapi/v2/tasks?page=1&size=20
Scope: user.task.readable
```

- page 默认 1
- size 默认 20
- size 最大 100
- 列表不返回 token / expire_at

## 查询单个任务

```text
GET /openapi/v2/tasks/{task_id}
Scope: user.task.readable
```

用于：

- 查询状态
- 获取/刷新 ACP link 和 token
- ACP 返回 401 后重新获取凭据

## 当前状态枚举

官方当前文档列出：

- CREATING
- idle
- planning
- working
- pending
- completed
- failed
- archived
- deleted

客户端不要只把 `completed/failed` 当成唯一状态集合。
