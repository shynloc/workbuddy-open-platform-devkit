# MCP Connector Template

默认示例使用 `streamableHttp + token` 思路，但 `connector-meta.json` 当前未开启 auth_mode。按你的服务实际认证方式修改。

## 文件

- connector-meta.json
- mcp.json
- token-schema.json（仅 auth_mode=token 时需要）
- icon.svg
- skills/example-connector/SKILL.md

## 如果使用 Token 模式

在 connector-meta.json 加：

```json
"auth_mode": "token",
"minWorkbuddyVersion": "4.24.0"
```

当前模板已经用了 examples_zh/examples_en，因此最低版本至少是 4.24.0。

确保：

`token-schema.json fields[].key == mcp.json 中 ${VAR} 占位符`

## 校验

```bash
python3 scripts/validate_connector.py <connector-directory>
```

提交前重新核验：
https://open.workbuddy.cn/docs/connector
