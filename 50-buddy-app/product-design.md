---
title: Buddy App Product Design Guide
knowledge_type: DERIVED
official_sources:
  - workbuddy-buddy-app
last_verified: 2026-10-08
status: VERIFIED
---

# Buddy App 产品设计

官方当前文档强调“场景优先”，并建议先梳理目标用户至少 5 个高频场景。

> **注意：官方同一页面目前对工作模式数量存在两处不同建议。**  
> 首页配置表写“建议配置 3–5 个”；最佳实践又写“建议 2–4 个”。见 `sources/known-inconsistencies.md`。  
> WB-OPDK 不替官方消解冲突：产品设计阶段优先追求模式职责清晰，MVP 可从 2–3 个明显不同的模式起步；最终配置数量以当前开放平台界面和提交校验为准。

## 1. Requirement Canvas

```text
Target User:
Industry:
Core Job-to-be-Done:

Top 5+ High-frequency Scenarios:
1.
2.
3.
4.
5.

Work Modes:
1.
2.
3.
4.
5.

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

先做最小可用版本，验证至少 5 个高频场景与少量职责明显不同的工作模式，再扩展市场、连接器与模型组合。
