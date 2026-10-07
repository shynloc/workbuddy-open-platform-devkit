# MCP + Token Connector Template

这是“远程 MCP + 用户自填 Token/API Key”的 WorkBuddy Connector 起点。

## 当前模板使用的最低版本

模板同时使用：

- `auth_mode: token`（≥4.23.0）
- `examples_zh/examples_en`（≥4.24.0）

因此模板默认：

```json
"minWorkbuddyVersion": "4.24.0"
```

## 使用

1. 修改 connector-meta.json
2. 修改 mcp.json URL / Server 名
3. token-schema key 与 `${VAR}` 占位符保持大小写完全一致
4. 不把真实 Token 写进仓库
5. 完善 skills/connector-usage/SKILL.md
6. 放置 icon.svg / icon.png / icon.jpg
7. 运行：

```bash
python3 scripts/validate_connector.py path/to/connector
```

官方来源：https://open.workbuddy.cn/docs/connector
