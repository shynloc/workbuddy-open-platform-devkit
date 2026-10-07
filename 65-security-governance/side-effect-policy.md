---
title: Side-effect Policy
knowledge_type: DERIVED
official_sources:
  - workbuddy-third-party-app
last_verified: 2026-10-08
status: VERIFIED
---

# Side-effect Policy

任何会改变外部世界状态的 Tool/API 都必须先分类。

## Risk levels

### R0 — Read-only

读取、搜索、预览。

通常不要求显式确认。

### R1 — Reversible write

创建草稿、创建未公开对象、添加可撤销标签。

可以根据用户明确任务执行，但要返回结果和回滚方式。

### R2 — External visible

发送邮件/消息、公开发布、邀请成员、创建外部日程。

默认需要用户意图足够明确；高影响场景建议显式确认。

### R3 — Destructive / privileged

永久删除、支付、权限变更、账号解绑、覆盖不可恢复数据。

必须显式确认，并在服务端再次校验权限。

## Confirmation quality

确认必须包含：

- action
- target
- scope
- irreversible consequence（如有）

不要问模糊的“确定吗？”。

## Idempotency

写操作出现网络超时时：

- 不直接重试未知结果的非幂等操作；
- 先查询当前状态；
- 使用 request/idempotency key（服务支持时）。

## Audit

R2/R3 操作建议记录：

- actor
- target
- timestamp
- request id
- result
- confirmation state

不要在审计日志保存敏感 Token。
