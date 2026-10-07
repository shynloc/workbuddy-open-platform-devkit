---
name: your-skill-name
display_name: 技能展示名称
display_name_en: Skill Display Name
description: 写清技能用途、触发条件与核心输出
description_zh: 简短中文介绍
description_en: Brief English introduction
category: writing
version: 1.0.0
author: Your Name
user-invocable: true
disable-model-invocation: false
---

# 技能名称

## 目标

说明这个 Skill 帮用户完成什么结果。

## 激活条件

当用户表达以下意图时使用：

- ...
- ...

## 工作边界

- 可以做：...
- 不应做：...
- 高风险动作：必须显式确认

## References

需要时读取：

- @references/example.md

## Workflow

1. Intake
2. Analyze
3. Execute
4. Validate
5. Deliver

## Error Handling

说明常见失败和恢复方式。

## Definition of Done

- [ ] 输出满足用户目标
- [ ] 必要校验已完成
- [ ] 未越过高风险确认边界
