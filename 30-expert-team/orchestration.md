---
title: Expert Team Orchestration Guide
knowledge_type: DERIVED
official_sources:
  - workbuddy-expert-team
last_verified: 2026-10-07
status: VERIFIED
---

# 专家团编排设计

Expert Team 应解决“真实需要多人专业分工”的任务，而不是为了看起来高级而复制多个 Agent。

## 1. Lead 的职责

主理人负责：

- 理解目标与交付标准；
- 拆解工作包；
- 决定并行/串行关系；
- 把任务分配给最合适成员；
- 处理冲突与缺口；
- 汇总最终交付；
- 控制不要重复劳动。

## 2. Member 的职责

每个成员必须拥有不可替代的明确域：

```text
Input Contract
→ 专业处理
→ Output Contract
```

成员之间如果 70% 以上职责重复，应合并角色。

## 3. 推荐拓扑

### Pipeline
Research → Draft → Review → Publish

### Parallel Research
Lead → [A, B, C] → Synthesis

### Debate
Evidence → Bull/Bear → Judge

### Review Gate
Producer → Reviewer → Lead Final

## 4. 上下文控制

共享长期规则放 skills/；只给成员它完成任务所需上下文，不让所有成员都重复阅读全部资料。

## 5. Definition of Done

团队结束时必须由 Lead 做一次最终验收，而不是直接拼接成员输出。
