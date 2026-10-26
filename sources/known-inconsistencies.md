# Known Upstream Inconsistencies

本文件记录 WorkBuddy 官方文档内部、官方文档与官方模板、或官方文档与当前平台行为之间的已知差异。目的不是替官方选择答案，而是防止 Agent 静默把冲突内容“合理化”。

## 2026-10-26 — Skill 历史字段待核实（共同缺失，不是双语冲突）

中文与英文 Skill 正文均明确要求 `name`、`display_name`、`display_name_en`，两页均未列出 `user-invocable` 与 `disable-model-invocation`。缺失只能说明当前文档未说明，不能推断平台弃用。Schema 与模板保留历史字段；提交前核实平台行为。双语监测以 `missing_in_both` 单独报告此信号，不再把它称为语言不一致。

## 2026-10-08

### Expert Team：Lead 设置文件名 — 已由真实平台解析裁决

上游仍存在文档/模板差异：

- 官方 Expert Team 页面基础结构：`settings.json`（复数），并标注为必须；
- 同页官方可下载 `trading-team.zip`：历史上实际包含 `setting.json`（单数）。

官方下载模板中的内容：

```json
{
  "agent": "trading-team-lead"
}
```

官方模板审计证据：

- `trading-team.zip` SHA256：`4935e7b86b7d32c47d03bb7c70c24adc29a41dc7d74fb9a97596e6d5a3e04345`
- `trading-team/setting.json` SHA256：`168767b04cffdc12b5c9f6b61d6a110208d58c3e0a1699dffa6e61a8091ca23b`

#### Real platform observation — 2026-10-08

真实候选 `ai-editorial-team-v1.0.0.zip` 仅提供 `setting.json` 时，WorkBuddy 开放平台解析失败：

```text
settings.json 不存在或无法读取（Team 型专家必须在 plugin root 下提供 settings.json）
```

因此当前执行规则已经明确：

1. **Team plugin root 必须使用 `settings.json`（复数）**；
2. 不再把 `setting.json` 视为可接受 fallback；
3. WB-OPDK Starter / Validator / Candidate 已全部改为 `settings.json`；
4. `settings.json` 当前使用官方模板已知的 `{"agent":"<lead>"}` 结构；
5. 官方 downloadable ZIP 应视为与当前 parser 不一致的上游资产，等待官方更新。

这是一条 `OFFICIAL page + OBSERVED runtime` 双重支持的规则。

### Expert Team：tags 数量

- 官方 Expert Team 字段表：`tags` 固定 3 个。
- 同页 `trading-team` 示例：当前展示了 4 个 tags。

处理原则：

1. 文档生成器默认按字段表输出 3 个 tags；
2. 提交当天重新检查开放平台解析/字段校验；
3. 若运行时与字段表冲突，记录为 `OBSERVED`，不要静默改知识库中的 `OFFICIAL` 结论。

### Buddy App：工作模式推荐数量

当前同一官方 Buddy App 页面存在两处不同建议：

- “首页配置 → 工作模式”：写“建议配置 3–5 个”；
- “最佳实践 → 精简工作模式”：写“建议 2–4 个”。

处理原则：

1. 不把任何一处改写成唯一官方结论；
2. 产品设计层优先减少职责重叠、控制用户选择成本；
3. MVP 可从 2–3 个差异明显的模式开始；
4. 实际提交时以开放平台当前 UI、校验和审核要求为准。

### Open API：Token 有效期

2026-10-20 复核，两处写法都还在：

- 第三方应用页 Token 表：access_token 24 小时，refresh_token 60 天
- Open API token 接口示例：`expires_in` 为 3600

调用方以 `/openapi/v2/token` 实际响应中的 `expires_in` 为准：

- 客户端不得把 access_token 时长写死；
- 用响应里的 `expires_in` 驱动缓存与刷新；
- refresh_token 仍按第三方应用页要求保存在服务端；
- 如果业务依赖精确 TTL，提交前应向官方确认。

### 第三方应用类型 vs Open API 准备工作 — 2026-10-20

第三方应用页当前写「开放平台当前支持两类第三方应用」：

- 硬件接入
- 积分兑换

该页类型表不再列出 Buddy 应用，「积分应用」标题已改为「积分兑换」。

同一时期的 Open API 页仍写：

- 准备工作：已创建的第三方应用，如硬件应用或 Buddy 应用
- 授权参数：回调地址和 scope 必须落在「硬件接入」或「Buddy 应用」已配置的集合内

处理原则：

1. 不把 Buddy 应用从产品地图或 Buddy App 文档里删掉；
2. 不把 Open API 页的「Buddy 应用」改写成「积分兑换」；
3. 积分兑换应用的权限上限以第三方应用页为准：仅积分与权益类 Scope。

### 分享签名填充 — 2026-10-20

第三方应用页同一文档里有两种填充描述：

- 「生成密钥」：RSA-2048、PKCS#8 PEM，并写签名算法为 RSAwithSHA256、PSS 填充
- 「PC端开发手册」的签名步骤：RS256，RSA PKCS#1 v1.5 填充、SHA-256；同页示例代码使用 `RSA_PKCS1_PADDING`

处理原则：

1. 不把其中一句改成唯一官方算法；
2. 签名步骤和示例彼此一致，密钥生成段与它们不一致；
3. 生产验签依赖填充方式时，先向官方确认当前验签实现接受哪一种。

### Open API：user.credit.readable

当前英文 Open API Reference 的个人额度读取接口曾标注 Scope 为 `user.credit.readable`。

但第三方应用页面当前公开的 Scope 列表未列出该 Scope，只列出 `user.credit.exchange` 等。

处理原则：

- 不默认认为所有第三方应用都可申请 `user.credit.readable`；
- 以当前开放平台应用权限管理页面实际可选 Scope 为准；
- 若目标产品需要读取额度，提交前确认应用类型是否开放该权限。
