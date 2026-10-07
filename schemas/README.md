# Machine-readable Schemas

这些 JSON Schema 是 **WB-OPDK 的 DERIVED 工程资产**，用于本地/CI 校验和 IDE 辅助。

它们不是 WorkBuddy 官方发布的 canonical schema，也不能替代开放平台实际解析器。

## 当前 Schema

- `skill-frontmatter.schema.json`
- `expert-plugin.schema.json`
- `expert-team-plugin.schema.json`
- `connector-meta.schema.json`
- `token-schema.schema.json`
- `release-manifest.schema.json`

## 使用原则

1. Schema 只固化已经由官方文档/模板明确支持、且我们已经验证过的结构。
2. 官方内部存在冲突的字段，不应过度收紧；相关差异见 `sources/known-inconsistencies.md`。
3. 提交前仍要运行产品专用 Validator 和 WorkBuddy 实际 Runtime Test。
