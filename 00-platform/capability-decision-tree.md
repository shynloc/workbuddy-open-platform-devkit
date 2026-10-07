---
title: WorkBuddy Product Type Decision Tree
knowledge_type: DERIVED
official_sources:
  - workbuddy-open-platform-overview
last_verified: 2026-10-07
status: VERIFIED
---

# 产品类型决策树

WorkBuddy 开放平台当前面向生态开发者提供 Skill、Expert、Expert Team、Connector、外部应用等产品能力；Buddy App 进一步提供垂直行业 AI 工作台的配置方式。

## 快速决策

### Skill
当核心价值是“教 AI 如何完成一类任务”，主要资产是 SOP、Prompt、references、scripts、templates 时，优先做 Skill。

### Expert
当用户需要的是“一个固定身份、专业方法论与工作习惯的人”时，做 Expert。Expert 可以携带 Skill，也可以声明外部依赖。

### Expert Team
当任务必须由多个独立专业角色真实分工协作，并由主理人编排和汇总时，做 Expert Team。不要为了市场包装而把一个单 Agent 强拆成多人。

### Connector
当价值来自外部系统、账号、数据或操作能力，例如 MCP、SaaS API、企业系统时，做 Connector。方法论可通过配套 Skill 提供。

### Buddy App
当目标是面向一个行业或工作领域提供完整的 AI Harness：工作模式、场景、专家、技能、连接器、模型配置等组合体验时，做 Buddy App。

### Third-party App / Open API
当你的独立网站、移动 App、硬件或 SaaS 需要调用 WorkBuddy 的本地助理、云端任务、ACP 或会话产物时，走第三方应用与 Open API。

## 组合不是冲突

一个成熟产品可以同时包含多层资产：

```text
Buddy App
├── Expert / Expert Team
├── Skills
├── Connectors
└── Open API integration
```

判断时先找“核心价值发生在哪一层”，再决定其他层是否作为增强能力。
