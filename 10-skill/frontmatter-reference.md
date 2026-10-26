---
title: WorkBuddy Skill Frontmatter Reference
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-skill
last_verified: 2026-10-26
status: VERIFIED
---

# Skill Frontmatter

按当前官方字段整理的可解析示例：

```yaml
---
name: your-skill-name
display_name: 展示名称
display_name_en: Display Name
description: 一句话描述技能能力
description_zh: 简短中文介绍
description_en: A Brief English Introduction
examples_zh:
  - "执行示例任务"
examples_en:
  - "Run the example task"
version: 1.0.0
author: 合作方名称
---
```

官方字段表：

| 字段 | 必填 | 含义 |
|---|---:|---|
| name | 是 | 技能标识 |
| display_name | 是 | 技能在市场上的中文展示名称 |
| display_name_en | 是 | 技能在市场上的英文展示名称 |
| description | 是 | 用途 + 触发词 |
| description_zh | 是 | 中文简介 |
| description_en | 是 | 英文简介 |
| allowed-tools | 否 | 工具白名单，逗号分隔 |
| version | 是 | 版本 |
| examples_zh | 否 | 中文使用案例，展示在详情页「试试这样用」 |
| examples_en | 否 | 英文使用案例，展示在详情页「试试这样用」 |
| author | 是 | 合作方名称 |

2026-10-26 复核[中文](https://open.workbuddy.cn/docs/skill)和[英文](https://open.workbuddy.cn/en/docs/skill)正文，两页均明确要求三项名称字段。现有 WB-OPDK 模板已提供这三项；本次修复知识库与校验遗漏，不表示已发布 Skill 损坏。

## 历史字段：当前支持状态待核实

两种语言当前均未列出 `user-invocable`、`disable-model-invocation`，这不是两种语言之间的不一致，也不能证明平台已弃用它们。Schema 继续接受这两个布尔字段，模板保留已有配置；发布前应在当前平台验证。

此前 KB 记录的含义为：`disable-model-invocation: true` 禁止模型自动触发；`user-invocable: false` 隐藏菜单、供 AI 内部使用。这些含义保留作历史参考，不能视为当前官方保证。`category` 也不在当前 Skill 字段表中，不作为必填字段。
