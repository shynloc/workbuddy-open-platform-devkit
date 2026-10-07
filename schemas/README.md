# Machine-readable Schemas

这些 JSON Schema 是 **WB-OPDK 的 DERIVED 工程资产**，用于本地/CI 校验和 IDE 辅助。

它们不是 WorkBuddy 官方发布的 canonical schema，也不能替代开放平台实际解析器。

## 当前 Schema

### Skill / Expert / Team

- `skill-frontmatter.schema.json`
- `agent-frontmatter.schema.json`
- `expert-plugin.schema.json`
- `expert-team-plugin.schema.json`

### Connector

- `connector-meta.schema.json`
- `mcp-config.schema.json`
- `cli-config.schema.json`
- `token-schema.schema.json`

### Release Engineering

- `release-manifest.schema.json`

## 使用原则

1. Schema 只固化已经由官方文档/模板明确支持、且我们已经验证过的结构。
2. 官方内部存在冲突的字段，不应过度收紧；相关差异见 `sources/known-inconsistencies.md`。
3. 跨字段、文件存在性、版本门槛、头像尺寸等规则由专用 Validator 处理。
4. 提交前仍必须经过 WorkBuddy 实际解析器、Runtime Test 和平台审核。
