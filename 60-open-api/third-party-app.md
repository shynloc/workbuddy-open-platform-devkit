---
title: WorkBuddy Third-party App
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-third-party-app
  - workbuddy-openapi
last_verified: 2026-10-27
status: VERIFIED
---

# 第三方应用

官方来源：

- https://open.workbuddy.cn/docs/third-party-app
- https://open.workbuddy.cn/docs/openapi

WorkBuddy 第三方应用页现在分成两条路径：

1. OAuth 2.1 应用，通过 HTTPS Open API 访问用户授权范围内的能力；
2. 分享能力，把用户内容预填到 WorkBuddy 任务输入区。协议见 `share-to-workbuddy.md`。

## 当前 OAuth 应用类型

第三方应用页当前写明开放平台支持两类第三方应用：

| 类型 | 创建入口 | 权限 |
|---|---|---|
| 硬件接入 | 「硬件接入」 | 全部已公开权限，按业务需要申请 |
| 积分兑换 | 「其他 > 积分兑换」 | 仅开放积分与权益类 Scope |

「积分应用」这一标题已从该页移除，当前标题是「积分兑换」。硬件接入的典型设备仍是智能眼镜、车机等。

Buddy 应用不再出现在这张类型表里。Open API 页的准备工作和授权参数仍写「硬件应用或 Buddy 应用」，两边不要互相改写。见 `sources/known-inconsistencies.md`。

## 能力域

OAuth 应用页当前列出的能力域：

- 本地助理对话
- 云端任务管理
- 产物管理
- 兑换码核销

## OAuth 应用流程

1. 一次性填写基本信息、权限管理和 OAuth 回调地址
2. 提交审核
3. 审核通过后状态为「已启用」
4. 引导用户完成 OAuth 2.1 授权
5. 服务端换取 token
6. 调用 Open API

官方状态表：审核中、已启用、已驳回。驳回后按反馈修改再提交。

## 凭据

官方当前写：应用创建后进入审核状态，平台生成 `client_id` 和 `client_secret`。`client_secret` 只在应用创建成功后明文展示一次，不得出现在前端或客户端代码中。遗失需联系平台。

分享能力使用另一套本地生成的 RSA 私钥和 `kid`，不是这对 client 凭据。

## Token

不要把 access_token 有效期写死。

第三方应用页的 Token 表当前写 access_token 24 小时、refresh_token 60 天。Open API 的 token 端点仍返回 `expires_in`，示例值为 3600 秒。调用方以实际响应中的 `expires_in` 为准，并安全保存 refresh_token，通过同一个 `/openapi/v2/token` 刷新。

响应字段仍是：

- `access_token`
- `token_type`
- `expires_in`
- `refresh_token`
- `scope`
- `open_id`

## Scope

公开列表未变：`user.profile.readable`、`user.contact.readable`、`user.credit.exchange`、`user.task.invokable`、`user.task.readable`、`user.localassistant.invokable`、`user.localassistant.readable`。

这一节的标题已从「权限配置列表及关联 API」改为「权限配置」。权限申请指南现在写明：硬件接入应用可按业务需要申请全部 Scope；积分兑换应用仅开放部分权限（如积分与权益类 `user.credit.exchange`），不提供其他能力域的权限选项。这仍不是默认全选的理由。最小权限原则的三句话还在。
