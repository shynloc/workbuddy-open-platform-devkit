---
title: Trust Boundaries
knowledge_type: DERIVED
official_sources:
  - workbuddy-third-party-app
last_verified: 2026-10-08
status: VERIFIED
---

# Trust Boundaries

官方定义的核心参与者：

- Resource Owner：WorkBuddy 用户
- Third Application：第三方应用
- WorkBuddy：代表用户执行任务/工具调用的 Agent Runtime
- Open Platform：应用注册、授权、Token、Scope、审计的可信边界

## Engineering model

```text
User
 │ explicit authorization
 ▼
Open Platform
 │ scoped token
 ▼
Third-party backend / Connector
 │ task/tool request
 ▼
WorkBuddy Runtime / External Service
```

任何设计都要回答：

- 谁是数据所有者？
- 谁在调用？
- 调用凭据代表谁？
- 能访问哪些数据？
- 谁批准了写操作？
- 用户撤销授权后怎么办？

## Anti-pattern

不要用一个供应商全局管理员 Token 让所有终端/用户共享同一权限上下文。
