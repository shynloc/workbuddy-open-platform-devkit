---
title: Hardware Runtime Paths
knowledge_type: DERIVED
official_sources:
  - workbuddy-openapi
last_verified: 2026-10-08
status: VERIFIED
---

# Hardware Runtime Paths

## Path A — Local Assistant

适合：

- 设备作为用户 PC WorkBuddy 的远程入口；
- 用户希望任务在本地 Agent 环境执行。

建议：

```text
Check Local Assistant Online
→ Send Message
→ Poll/Read Message History
→ Surface Result on Device
```

本地助理离线不是 API 服务异常，应提供“PC WorkBuddy 未在线”的明确状态。

## Path B — Cloud Task

适合：

- PC 不在线仍需运行；
- 任务需要云端持续执行；
- 移动/硬件端需要会话续接。

```text
Create Task
→ Query until ACP link/token ready
→ Connect ACP
→ Stream events
→ Retrieve artifacts
```

## Path C — Artifacts

硬件 UI 不应只消费聊天文本。

会话产物可以用于展示：

- plan
- tasks
- media
- overview

恢复会话时推荐：

```text
REST full snapshot
→ index by artifact.uri
→ ACP/SSE incremental updates
```

## Resilience

必须覆盖：

- device network loss
- token expiry
- ACP reconnect
- duplicate event
- user cancellation
- local assistant offline
