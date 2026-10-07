---
title: Cloud Task API
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-openapi
last_verified: 2026-10-08
status: VERIFIED
---

# 云端任务 API

官方来源：https://open.workbuddy.cn/docs/openapi

## 1. 创建任务

当前官方 endpoint：

```text
POST https://www.workbuddy.cn/openapi/v2/tasks
```

Scope：

```text
user.task.invokable
```

请求体：

- `prompt`：必填，任务初始指令
- `name`：可选，不传时服务端按 prompt 生成

返回可能包含：

- task_id
- status
- name
- link（ACP 地址）
- token（ACP 鉴权）
- expire_at
- sandboxLink
- sandboxDataLink

创建成功但暂时没有 link/token 时，官方建议轮询“查询任务”接口直到补齐。

## 2. 查询任务列表

```text
GET /openapi/v2/tasks?page=1&size=20
```

Scope：

```text
user.task.readable
```

官方当前规则：

- page 默认 1
- size 默认 20
- size 最大 100
- 列表不返回 ACP token / expire_at

## 3. 查询单任务

```text
GET /openapi/v2/tasks/{task_id}
```

Scope：`user.task.readable`

用于读取最新状态以及获取/刷新 ACP link/token。

## 4. status 当前枚举

- CREATING
- idle
- planning
- working
- pending
- completed
- failed
- archived
- deleted

客户端不要只处理 completed/failed 两种状态。
