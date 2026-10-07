---
title: Hardware Device Security
knowledge_type: DERIVED
official_sources:
  - workbuddy-third-party-app
  - workbuddy-openapi
last_verified: 2026-10-08
status: VERIFIED
---

# Device Security

## Secrets

设备端禁止内置：

- WorkBuddy client_secret
- 长期 refresh_token
- 供应商生产环境管理员 Token
- 可跨用户复用的全局凭据

## Session

设备只持有短生命周期、最小权限会话材料。

设备丢失/解绑后，应能服务端撤销设备与用户的关联。

## Storage

需要持久化的本地数据：

- 最小化
- 加密（平台能力允许时）
- 与设备锁屏/用户态绑定
- 恢复出厂时清除

## Logs

硬件日志不要记录：

- Authorization header
- OAuth code
- access_token / refresh_token
- ACP ticket
- 用户完整对话正文（除非产品明确需要且有合规依据）

## Physical threat model

硬件比普通 Web App 多一层现实风险：

- 丢失
- 借用
- 维修
- 二手转让
- 恢复出厂
- 多人共用车辆/终端

产品必须设计“退出 WorkBuddy / 解除绑定 / 清除本地状态”的路径。
