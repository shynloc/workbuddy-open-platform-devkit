---
title: Expert Team settings.json Status
knowledge_type: OFFICIAL
last_verified: 2026-10-07
status: VERIFIED
official_sources:
  - workbuddy-expert-team
---

# settings.json

官方 Expert Team 目录结构明确要求根目录存在 `settings.json`，用途是“设置主理人”。

截至本次核验，公开页面正文没有给出该文件的完整字段 schema；官方提供 `trading-team.zip` 作为模板下载。

因此 WB-OPDK 暂时不提供猜测版 `settings.json` 模板。

## 规则

- 不根据 CodeBuddy CLI 的项目级 settings.json 猜 Expert Team settings.json；两者不是同一上下文。
- 生成 Expert Team 发布包时，必须从当前官方模板或当前开放平台创建工具得到可验证格式。
- 一旦字段被官方页面明确公开或官方模板内容被验证，本文件再升级为正式 schema reference。
