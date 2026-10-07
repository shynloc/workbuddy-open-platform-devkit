---
title: connector-meta.json Reference
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-connector
last_verified: 2026-10-08
status: VERIFIED
---

# connector-meta.json

官方来源：https://open.workbuddy.cn/docs/connector

## 当前字段

| 字段 | 状态 | 说明 |
|---|---|---|
| name / name_en | 必填 | 默认名称与英文名称 |
| name_zh | 可选/新版本 | 中文名称 |
| description / description_zh / description_en | 必填 | 核心能力与适用场景 |
| source | 必填 | 全局唯一，小写字母/数字/连字符 |
| type | 可选 | mcp（默认）/ cli / skill-only |
| version | 建议 | SemVer |
| examples_zh / examples_en | 新版本必需 | 自 4.24.0 |
| auth_mode | 按需 | 省略/server-side/gateway/token |
| minWorkbuddyVersion | 使用新字段时必填 | 自 4.22.12 |
| maxWorkbuddyVersion | 可选 | 紧急停用上限 |
| name_map / description_map | 可选 | 自 5.2.0 |

## 展示回退

名称优先级：

```text
name_map 命中
→ name_zh
→ name_en
→ name
```

描述同理回退。

## 写作原则

- 名称可辨认；
- 描述直接写“用户能完成什么”；
- examples 使用真实自然语言；
- 使用任意新版本字段时，把 minWorkbuddyVersion 提升到这些字段要求中的最高版本。
