---
title: Expert plugin.json Reference
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-expert
last_verified: 2026-10-08
status: VERIFIED
---

# Expert plugin.json Reference

本文件是字段导航，不替代官方文档。提交前应再次核验：
https://open.workbuddy.cn/docs/expert

## 字段分组

### Identity

- name
- expertType = agent
- version
- description
- author
- homepage
- license
- keywords

### Runtime

- agents
- agentName
- skills（可选）
- dependencies（如需要）

### Marketplace

- displayName
- profession
- displayDescription
- avatar
- categoryId
- defaultInitPrompt
- plugin
- tags（当前官方要求固定 3 个）
- quickPrompts（当前官方要求固定 3 个）

## 关键一致性约束

- plugin 必须与 name 一致；
- agentName 必须能解析到 agents 中的主 Agent；
- defaultInitPrompt 与 quickPrompts 第一条一致；
- Agent MD frontmatter 的 name 与文件名一致；
- avatar 路径必须存在；
- skills/dependencies 声明必须有真实文件或可安装依赖。
