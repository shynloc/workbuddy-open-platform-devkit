---
title: Connector High-risk Tool Design
knowledge_type: DERIVED
official_sources:
  - workbuddy-connector
last_verified: 2026-10-08
status: VERIFIED
---

# 高风险 Tool 设计

Connector 的技术“可调用”不等于 Agent 可以无条件调用。

## 需要确认的典型动作

- 发布/发送到公众
- 删除
- 永久删除
- 覆盖远端数据
- 支付/下单
- 权限变更
- 外部邀请
- 账户绑定/解绑
- 批量修改

## 推荐设计

1. Tool 名称清楚体现副作用；
2. Tool description 写清不可逆性；
3. 参数中有明确的目标 ID；
4. 重大动作增加 `confirmed` 等显式字段（如果服务端设计允许）；
5. Skill 再增加行为确认规则；
6. 服务端做权限校验，不把安全只寄托在 Prompt。

## 禁止

- 用模糊 Tool 名隐藏副作用；
- Agent 根据“继续/弄好”推断发布或永久删除；
- 错误日志输出完整 Token；
- 用全局管理员密钥替代用户级权限隔离。
