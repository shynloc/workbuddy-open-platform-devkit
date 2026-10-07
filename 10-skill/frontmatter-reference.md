---
title: WorkBuddy Skill Frontmatter Reference
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-skill
last_verified: 2026-10-07
status: VERIFIED
---

# Skill Frontmatter

官方当前示例：

```yaml
---
name: your-skill-name
display_name: 展示名称
display_name_en: Display Name
description: 一句话描述技能能力
description_zh: 简短中文介绍
description_en: A Brief English Introduction
category: writing
version: 1.0.0
author: 合作方名称
---
```

官方字段表：

| 字段 | 必填 | 含义 |
|---|---:|---|
| name | 否 | 技能标识 |
| description | 是 | 用途 + 触发词 |
| description_zh | 是 | 中文简介 |
| description_en | 是 | 英文简介 |
| allowed-tools | 否 | 工具白名单，逗号分隔 |
| version | 是 | 版本 |
| disable-model-invocation | 否 | true 时禁止模型自动触发 |
| user-invocable | 否 | false 时隐藏菜单，仅供 AI 内部使用 |
| author | 是 | 合作方名称 |

当前官方示例还包含 `display_name`、`display_name_en`、`category`。这些字段出现在示例但不在同页“必填字段表”中；生成器可保留，但不要把它们错误标成必填。
