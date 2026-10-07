---
title: OAuth and Scope Governance
knowledge_type: DERIVED
official_sources:
  - workbuddy-third-party-app
  - workbuddy-openapi
last_verified: 2026-10-08
status: VERIFIED
---

# OAuth & Scope Governance

## Official baseline

第三方应用：

- 用户数据访问前需要显式授权；
- OAuth 2.1 authorization code flow；
- Scope 由应用权限配置和用户授权共同限制；
- 官方明确要求最小权限。

## Engineering rules

### Registration-time Scope

只申请产品必须具备的能力上限。

### Request-time Scope

授权时只请求当前操作真正需要的子集。

### Runtime check

不要因为应用“申请过”某 Scope，就假定当前 token 一定包含它；应以实际授予的 `scope` 为准。

### Scope expansion

新版本新增高权限功能时：

- 视为权限模型变化；
- 更新隐私/审核说明；
- 触发重新授权；
- 不静默提升历史用户权限。

## Scope → feature map

建议每个 Third-party App 维护：

| Feature | Scope | Read/Write | User-visible side effect | Why required |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
