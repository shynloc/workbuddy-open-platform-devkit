---
title: WorkBuddy Third-party App
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-third-party-app
  - workbuddy-openapi
last_verified: 2026-10-07
status: VERIFIED
---

# 第三方应用

官方来源：

- https://open.workbuddy.cn/docs/third-party-app
- https://open.workbuddy.cn/docs/openapi

WorkBuddy 第三方应用使用 OAuth 2.1 完成用户认证授权，并通过 HTTPS Open API 访问用户授权范围内能力。

## 当前应用类型

官方当前列出：

- 硬件接入
- Buddy 应用
- 积分应用

## 能力域

- 本地助理对话
- 云端任务管理
- ACP 实时通道
- 会话产物
- 积分/兑换码能力

## 应用流程

1. 创建应用
2. 配置基本信息
3. 配置 Scope
4. 配置 OAuth 回调
5. 提交审核
6. 审核通过/启用
7. 引导用户授权
8. 服务端换取 token
9. 调 Open API

## 凭据

平台生成 `client_id` / `client_secret`。官方说明 client_secret 只明文展示一次，不得暴露在前端或客户端代码。

## Token

不要把 access_token 有效期写死。

Open API 的 token 端点会返回：

- `access_token`
- `token_type`
- `expires_in`
- `refresh_token`
- `scope`
- `open_id`

调用方应以**实际响应中的 `expires_in`**作为 access_token 有效期来源，并安全保存 refresh_token，在需要时通过同一 `/openapi/v2/token` 端点刷新。

> 当前官方文档不同示例中的 `expires_in` 数值并不完全一致，因此本仓库不把某个固定时长当成协议常量；以接口响应为准。
