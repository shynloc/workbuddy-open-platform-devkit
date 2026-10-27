---
title: WorkBuddy Skill Frontmatter Reference
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-skill
last_verified: 2026-10-27
status: VERIFIED
---

# Skill Frontmatter

官方当前示例（中英文页面相同，含页面上的两处写法）：

```yaml
---
name: your-skill-name
display_name: 展示名称
display_name_en:切英文版展示名称
description: 一句话描述技能能力
description_zh: 简短中文介绍
description_en: A Brief English Introduction
examples_zh:
- "案例 1"
- "案例 2"
- "案例 3"
examples_en:
- "example 1"
- "exmaple 2"
- "example 3"
version: 1.0.0
author: "合作方名称"
---
```

`display_name_en:切英文版展示名称` 和 `exmaple` 按官方示例原样保留。提交用的模板另写正常英文展示名，见 `sources/known-inconsistencies.md`。

官方字段表：

| 字段 | 必填 | 含义 |
|---|---:|---|
| name | 是 | 技能标识 |
| display_name | 是 | 市场上的中文展示名称 |
| display_name_en | 是 | 市场上的英文展示名称 |
| description | 是 | 写清用途和触发词 |
| description_zh | 是 | 简短中文介绍，展示在技能详情页 |
| description_en | 是 | 简短英文介绍，展示在技能详情页 |
| allowed-tools | 否 | 工具白名单，逗号分隔 |
| version | 是 | 版本号 |
| examples_zh | 否 | 中文使用案例，展示在详情页「试试这样用」 |
| examples_en | 否 | 英文使用案例，展示在详情页「试试这样用」 |
| author | 是 | 合作方名称 |

上一版字段表里的 `name: 否`、`disable-model-invocation`、`user-invocable`，以及示例里的 `category: writing`，在 2026-10-27 的中英文页面都已不在。
