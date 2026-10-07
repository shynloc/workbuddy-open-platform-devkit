# Known Upstream Inconsistencies

本文件记录 WorkBuddy 官方文档内部、官方文档与官方模板、或官方文档与当前平台行为之间的已知差异。目的不是替官方选择答案，而是防止 Agent 静默把冲突内容“合理化”。

## 2026-10-07

### Expert Team：Lead 设置文件名

- 官方 Expert Team 页面基础结构写：`settings.json`（复数），说明为“设置主理人（必须）”。
- 同页官方可下载模板 `trading-team.zip` 实际包含：`setting.json`（单数）。
- 该官方模板中的实际内容：

```json
{
  "agent": "trading-team-lead"
}
```

本次审计证据：

- 官方 `trading-team.zip` SHA256：`4935e7b86b7d32c47d03bb7c70c24adc29a41dc7d74fb9a97596e6d5a3e04345`
- `trading-team/setting.json` SHA256：`168767b04cffdc12b5c9f6b61d6a110208d58c3e0a1699dffa6e61a8091ca23b`

处理原则：

1. WB-OPDK Validator 接受 `setting.json` 或 `settings.json`，但不允许两者同时存在；
2. 当前 starter template 跟随官方可下载模板，使用 `setting.json`；
3. 如果使用 `setting.json`，`agent` 必须等于 `agentName/teamInfo.leadAgent`；
4. 发布当天仍应以开放平台实际解析结果为最终裁决。

### Expert Team：tags 数量

- 官方 Expert Team 字段表：`tags` 固定 3 个。
- 同页 `trading-team` 示例：当前展示了 4 个 tags。

处理原则：

1. 文档生成器默认按字段表输出 3 个 tags；
2. 提交当天重新检查开放平台解析/字段校验；
3. 若运行时与字段表冲突，记录为 `OBSERVED`，不要静默改知识库中的 `OFFICIAL` 结论。

### Open API：Token 有效期

第三方应用页当前明确写：

- access_token：24 小时
- refresh_token：60 天

但 Open API token 接口示例中的 `expires_in` 当前出现过不同数值（例如授权码交换与刷新示例并不一致）。

处理原则：

- 客户端不得把 access_token 时长写死；
- 以 `/openapi/v2/token` 实际响应中的 `expires_in` 驱动缓存与刷新；
- refresh_token 的持久化/失效策略应重新核对当前官方页面与实际响应；
- 如果业务依赖精确 TTL，提交前应向官方确认。

### Open API：user.credit.readable

当前英文 Open API Reference 的个人额度读取接口 `GET /openapi/v2/credit` 标注 Scope 为 `user.credit.readable`。

但第三方应用页面当前公开的 Scope 列表未列出该 Scope，只列出 `user.credit.exchange` 等。

处理原则：

- 不默认认为所有第三方应用都可申请 `user.credit.readable`；
- 以当前开放平台应用权限管理页面实际可选 Scope 为准；
- 若目标产品需要读取额度，提交前确认应用类型是否开放该权限。

### Buddy App：工作模式推荐数量

当前 Buddy App 文档首页配置处写明工作模式“建议配置 3–5 个”。如果本地旧文档写成 2–4，应标记为过期并更新。
