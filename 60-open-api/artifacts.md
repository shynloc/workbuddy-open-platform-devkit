---
title: Session Artifacts
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-openapi
last_verified: 2026-10-08
status: VERIFIED
---

# 会话产物

官方来源：https://open.workbuddy.cn/docs/openapi

云端会话可以产生计划、任务、媒体、总结等 artifacts。

## 事件

ACP/SSE 当前定义三种事件：

- `created`：新增，artifact 为完整对象
- `updated`：变更，artifact 为完整对象（不是 diff）
- `deleted`：删除，至少保证 type 与 uri

官方建议以 `artifact.uri` 为本地主键做 upsert/delete；重复 created 可按 updated 处理。

## REST 全量

```text
GET {sandbox_url}/api/session/artifacts
```

鉴权：

```http
Authorization: Bearer {task_ticket}
```

sandbox_url 来自任务 link 去掉末尾 ACP 路径段。

可按：

- type
- limit / offset
- startMs / endMs

等条件获取。

## 推荐同步模式

```text
进入会话
→ REST 拉全量
→ 按 uri 建索引
→ SSE 订阅增量
→ created/updated = upsert
→ deleted = delete
```

这种“REST 首屏 + SSE 增量”模式天然适合会话恢复。

task_ticket 过期返回 401 时，重新查询云端任务获得新票据后重试。
