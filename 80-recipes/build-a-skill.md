# Recipe: 从需求到 WorkBuddy Skill

## 输入

- 用户问题/业务 SOP
- 参考文档
- 预期输入输出
- 可选工具/脚本

## 步骤

1. 用 `70-release-engineering/requirement-intake.md` 明确 JTBD；
2. 判断是否真的是可复用 SOP，而非一次性任务；
3. 设计 SKILL.md 状态机/阶段；
4. 把长知识拆到 references；
5. 把确定性逻辑拆到 scripts；
6. 把标准产物拆到 templates；
7. 按 `10-skill/specification.md` 补全 frontmatter；
8. 跑 `10-skill/qa-checklist.md`；
9. 打 ZIP，在 WorkBuddy 实际解析；
10. 用至少 3 个真实自然语言案例做 runtime test；
11. 准备市场 icon 与发布资料；
12. 提交审核并记录反馈。

## Done

另一个 Agent 仅拿 Skill 包，不依赖原聊天也能稳定完成任务。
