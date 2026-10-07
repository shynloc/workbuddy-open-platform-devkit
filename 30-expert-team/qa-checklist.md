# Expert Team QA Checklist

## Package

- [ ] .codebuddy-plugin/plugin.json
- [ ] settings.json
- [ ] agents/
- [ ] avatars/
- [ ] skills/（如配置）
- [ ] .mcp.json（如配置）

## plugin.json

- [ ] expertType = team
- [ ] name / plugin 一致
- [ ] version 为 SemVer
- [ ] teamInfo 存在
- [ ] teamInfo.leadAgent 对应真实 Agent
- [ ] teamInfo.memberAgents 与 agents 文件一致
- [ ] members 包含 Lead + 所有 Member
- [ ] member id/name/avatar/profession/role 完整
- [ ] tags 正好 3 条
- [ ] quickPrompts 正好 3 条
- [ ] defaultInitPrompt = quickPrompts[0]

## Runtime

- [ ] settings.json 指向正确 Lead
- [ ] Lead 能拆解、派发、合并
- [ ] Member 职责明显不重叠
- [ ] Shared Skill 不重复塞入每个 Agent
- [ ] 依赖缺失时行为清楚
- [ ] 多成员失败时 Lead 能恢复

## Security

- [ ] .mcp.json 无真实凭据
- [ ] token 使用变量/用户配置
- [ ] 高风险外部操作有显式确认
