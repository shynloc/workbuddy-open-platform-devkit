---
title: WorkBuddy User and Credits APIs
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-openapi
  - workbuddy-third-party-app
last_verified: 2026-10-07
status: VERIFIED
---

# 用户资料、联系方式与积分

## 用户资料

```text
GET /openapi/v2/user/profile
Scope: user.profile.readable
```

当前中文官方文档返回：

- nickname
- avatar

## 验证联系方式

```text
POST /openapi/v2/user/phoneverification
Scope: user.contact.readable
```

接口只返回手机号是否匹配，不返回用户真实手机号或脱敏手机号。

## 读取个人额度

当前英文 Open API Reference 描述：

```text
GET /openapi/v2/credit
Scope: user.credit.readable
```

返回示例包含：

- total_capacity_size
- total_capacity_used

但 `user.credit.readable` 当前未出现在第三方应用页的公开 Scope 列表中。是否可申请应以开放平台应用权限页面为准。

## 核销兑换码

```text
POST /openapi/v2/redemptions
Scope: user.credit.exchange
```

支持：

- 单码：`code`
- 双码：`gift_key + gift_code`

同时必须提供 `request_id` 作为幂等/防重请求号。

成功响应当前包含：

- status
- flow_no
- credits
- open_id

## 安全原则

- 核销请求必须使用稳定、唯一的 request_id；
- 对 `invalid_grant` 等终态错误不要盲目重试；
- Scope 是否可申请必须以当前应用类型与开放平台权限管理页为准。
