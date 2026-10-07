# Expert QA Checklist

- [ ] .codebuddy-plugin/plugin.json 存在
- [ ] avatars/ 与 agents/ 路径正确
- [ ] expertType = agent
- [ ] name 为 kebab-case
- [ ] plugin 与 name 一致
- [ ] agentName 对应实际 Agent 文件
- [ ] agents 列表路径存在
- [ ] displayName / profession 中英双语
- [ ] displayDescription 中文 40–50 字
- [ ] tags 正好 3 条
- [ ] quickPrompts 正好 3 条
- [ ] defaultInitPrompt 与 quickPrompts[0] 一致
- [ ] avatar 512×512、≤500KB
- [ ] categoryId 合法
- [ ] Agent MD name 与文件名一致
- [ ] 专家未自行声明系统不允许的 tools
- [ ] skills 路径存在（如配置）
- [ ] dependencies 只在确有必要时声明
