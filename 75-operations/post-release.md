---
title: Post-release Operations
knowledge_type: DERIVED
official_sources:
  - workbuddy-open-platform-overview
last_verified: 2026-10-08
status: VERIFIED
---

# Post-release Operations

## First 24h / first release window

观察：

- 安装/召唤/连接是否正常
- OAuth/Token 错误
- Tool failure rate
- Runtime latency
- 用户不知道下一步的 UX 问题
- 审核后配置是否与提交版本一致

## Operational signals

建议至少有：

- version
- request/trace id
- error class
- latency
- dependency status
- auth failure count
- high-risk write failure count

不要求把用户正文收集进遥测。

## Feedback loop

用户反馈分类：

- Bug
- Official-spec mismatch
- Runtime incompatibility
- UX confusion
- Missing capability
- Security/privacy issue

具有普遍性的行为回灌 WB-OPDK 时标记 OBSERVED。

## Change control

线上发现问题不要直接“边修边猜”。

```text
Reproduce
→ classify
→ patch
→ local validation
→ runtime validation
→ release
→ observe
```
