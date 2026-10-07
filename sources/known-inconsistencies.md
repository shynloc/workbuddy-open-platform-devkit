# Known Upstream Inconsistencies

本文件记录 WorkBuddy 官方文档内部、或官方文档与当前平台行为之间的已知差异。目的不是替官方选择答案，而是防止 Agent 静默把冲突内容“合理化”。

## 2026-10-07

### Expert Team：tags 数量

- 官方 Expert Team 字段表：`tags` 固定 3 个。
- 同页 `trading-team` 示例：当前展示了 4 个 tags。

处理原则：

1. 文档生成器默认按字段表输出 3 个 tags；
2. 提交当天重新检查开放平台解析/字段校验；
3. 若运行时与字段表冲突，记录为 `OBSERVED`，不要静默改知识库中的 `OFFICIAL` 结论。

### Open API：access_token expires_in

Open API 当前不同 token 示例中的 `expires_in` 数值并不完全一致。

处理原则：

- 客户端不得把固定 access_token 时长写死；
- 以 `/openapi/v2/token` 实际响应中的 `expires_in` 为准；
- refresh_token 也应按接口实际行为和官方当前文档处理。

### Buddy App：工作模式推荐数量

当前 Buddy App 文档首页配置处写明工作模式“建议配置 3–5 个”。如果本地旧文档写成 2–4，应标记为过期并更新。
