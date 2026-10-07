# Expert Template

这是 WorkBuddy 单专家起点，不包含头像二进制文件。

## 使用

1. 替换 `.codebuddy-plugin/plugin.json` 中所有占位值；
2. 把 Agent 文件重命名并同步 `name / agents / agentName`；
3. 准备 `avatars/expert.png` 或 JPG：
   - 512×512
   - ≤500KB
4. 中文 displayDescription 调整到当前官方要求的 40–50 字；
5. tags 固定 3 条、quickPrompts 固定 3 条；
6. defaultInitPrompt 必须等于 quickPrompts[0]；
7. 运行：

```bash
python3 scripts/validate_expert.py path/to/expert
```

官方来源：https://open.workbuddy.cn/docs/expert
