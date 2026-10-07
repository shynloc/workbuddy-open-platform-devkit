---
title: Skill Development Workflow
knowledge_type: DERIVED
official_sources:
  - workbuddy-skill
last_verified: 2026-10-07
status: VERIFIED
---

# Skill 开发 SOP

## 1. Requirement Intake

先回答：

- 用户要让 AI 学会哪一类可复用任务？
- 触发条件是什么？
- 输入是什么？
- 输出是什么？
- 哪些知识需要 references？
- 哪些确定性工作适合 scripts？
- 哪些格式适合 templates？
- 是否依赖外部连接器？

## 2. 设计 SKILL.md

建议结构：

1. 目标与激活条件
2. 工作边界
3. 必读 references
4. Phase / Workflow
5. 工具/脚本调用规则
6. 错误处理
7. Definition of Done

核心要求：让另一个 Agent 不依赖原始聊天就能执行。

## 3. Progressive Disclosure

不要把所有知识塞进 SKILL.md。

- 高频决策留 SKILL.md；
- 长规范、字段枚举放 references；
- 重复性/确定性处理放 scripts；
- 可复用产物结构放 templates。

## 4. Validation

发布前检查：

- ZIP 顶层只有一个 skill 根目录；
- 根目录有 SKILL.md；
- frontmatter YAML 可解析；
- 必填字段齐全；
- @references 路径都存在；
- scripts 运行命令真实可执行；
- 不含凭据/本地绝对路径；
- version 使用语义化版本。

## 5. Runtime Test

至少验证：

- 明确触发能否命中；
- 相似但不相关场景不会乱触发；
- references 能读取；
- scripts 在 WorkBuddy Bash 环境运行；
- 没有可选依赖时是否有合理 fallback。
