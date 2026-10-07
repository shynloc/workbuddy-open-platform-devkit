---
title: Buddy App Product Design Guide
knowledge_type: DERIVED
official_sources:
  - workbuddy-buddy-app
last_verified: 2026-10-07
status: VERIFIED
---

# Buddy App 产品设计

官方最佳实践要求从高频场景出发，并建议先梳理至少 5 个高频场景、工作模式控制在 2–4 个。

## 1. Requirement Canvas

```text
Target User:
Industry:
Core Job-to-be-Done:
Top 5 High-frequency Scenarios:
1.
2.
3.
4.
5.

Work Modes (2-4):
1.
2.
3.
4.

Assets:
- Skills
- Experts / Teams
- Connectors
- Existing MCP Apps
- Models
```

## 2. 工作模式

模式不是“栏目”，而是模式级 Harness：

- System Prompt
- 绑定 Skill
- 模型策略
- 场景边界

模式之间应该有明显任务差异，否则应合并。

## 3. 场景胶囊

优先选择：

- 高频
- 用户知道结果但不知道怎么提问
- 能明显缩短启动成本
- 能绑定一个稳定流程/专家/Skill 的场景

## 4. 市场

不要把所有生态资产全塞进去。市场是“该行业用户应该发现什么”的策展层。

## 5. MVP

先做最小可用版本，验证 5 个高频场景，再扩展模式与市场。
