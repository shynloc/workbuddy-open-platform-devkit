---
title: Expert Product Design Guide
knowledge_type: DERIVED
official_sources:
  - workbuddy-expert
last_verified: 2026-10-07
status: VERIFIED
---

# Expert 设计指南

Expert 的价值不是“换一段 System Prompt”，而是让用户感到自己召唤了一个稳定、可预期的专业角色。

## 设计顺序

1. 用户是谁；
2. 这个专家替代/增强现实中的什么职业角色；
3. 专家能独立交付什么结果；
4. 哪些任务应该拒绝或转交；
5. 需要哪些 Skills；
6. 是否真的依赖外部 Connector；
7. 市场展示如何让用户在 5 秒内理解它。

## Agent 指令建议

至少定义：

- Role & Mission
- Scope
- Workflow
- Output Contract
- Quality Bar
- Tool/Skill Usage
- Safety / Confirmation
- Handoff

不要在 Agent MD 中复制大量领域资料；资料放 Skill references。

## 市场文案

- displayName：像一个“人/角色”或可识别专业名称；
- profession：一眼说明职业能力；
- displayDescription：40–50 中文字，写结果，不写空泛人格；
- tags：3 个高信号能力标签；
- quickPrompts：3 条用户真的会说的话；
- 第一条 quickPrompt = defaultInitPrompt。

## 依赖策略

能无连接器完成核心价值时，不要把 Connector 声明成强依赖；否则会增加召唤前门槛。

只有“没有外部系统就无法完成核心任务”时，才声明依赖。
