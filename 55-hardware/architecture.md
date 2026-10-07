---
title: Hardware Integration Architecture
knowledge_type: DERIVED
official_sources:
  - workbuddy-third-party-app
  - workbuddy-openapi
last_verified: 2026-10-08
status: VERIFIED
---

# 硬件接入架构

官方定义“硬件接入”为第三方应用类型，典型设备包括智能眼镜、车机等。

## 推荐分层

```text
Hardware Device
      │
      │ user interaction
      ▼
Vendor App / Device Client
      │
      │ short-lived session / app token
      ▼
Vendor Backend
      │
      │ OAuth 2.1 + client_secret (server-side only)
      ▼
WorkBuddy Open Platform
      │
      ├── Local Assistant
      ├── Cloud Tasks
      ├── ACP
      └── Session Artifacts
```

## 核心原则

- `client_secret` 只放服务端，不进入固件/前端；
- 设备端只持有完成当前会话所需的最小凭据；
- Scope 按业务功能申请；
- 硬件离线/PC 本地助理离线必须有明确 UX；
- 不把 WorkBuddy 的用户授权替换成设备厂商自己的“默认同意”。

## Device identity ≠ WorkBuddy user identity

硬件序列号、设备账号和 WorkBuddy 用户身份应分离管理。

设备被转卖、重置或解绑时，必须能撤销本地映射和令牌。
