---
title: Buddy App Model Strategy
knowledge_type: DERIVED
official_sources:
  - workbuddy-buddy-app
last_verified: 2026-10-08
status: VERIFIED
---

# 模型策略

Buddy App 的模型列表是产品体验的一部分，而不是“模型越多越好”。

## 推荐原则

- 默认模型覆盖最高频任务；
- 高成本/高能力模型用于复杂推理、审计、架构；
- 快速模型用于日常交互；
- 模式可以绑定适合的默认模型；
- 不把模型品牌当作用户工作流本身。

## Mode → Model

```text
Work Mode
→ 任务复杂度
→ 延迟要求
→ 上下文长度
→ 工具使用
→ 默认模型
```

## 验证

至少测试：

- 默认模型不可用时；
- 模型列表排序；
- 低成本模型是否能完成基础场景；
- 高规格模型是否真的带来质量增益。
