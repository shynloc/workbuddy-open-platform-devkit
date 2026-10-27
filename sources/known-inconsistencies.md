# Known Upstream Inconsistencies

本文件记录 WorkBuddy 官方文档内部、官方文档与官方模板、或官方文档与当前平台行为之间的已知差异。目的不是替官方选择答案，而是防止 Agent 静默把冲突内容“合理化”。

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

### 开放平台概述：测试步骤与品牌写法 — 2026-10-27

快速开始已去掉「在测试环境中进行调试和验证」。同页平台简介写成「面向Workbuddy生态业务」，平台优势仍写「WorkBuddy 生态」。

处理原则：

1. 概述页的官方步骤表按当前七步记录，不把测试环境调试写回官方快速开始；
2. 本仓库 SOP 里的 QA 继续保留，并标明是仓库要求；
3. 品牌名在仓库正文使用 WorkBuddy。概述页那一处 `Workbuddy` 保持为官方原文差异，不改写成唯一拼写。

### 入驻主体数量与开发者昵称 — 2026-10-27

同一入驻页有两套账号上限：

- 企业认证：每个账号最多认证 10 个企业主体；同一家企业最多 50 个账号；
- 其他组织机构认证：每个账号下非个人主体（企业主体与组织机构主体）合计最多 10 个；同一统一社会信用代码只能认证一个主体；同一组织最多 50 个账号。

昵称也有两套写法：

- 企业认证在上传企业信息时收集开发者昵称，并做命名规范校验；
- 组织机构认证写明流程不收集开发者昵称，认证后到「设置 → 开发者信息」填写，方可发布资产；
- https://open.workbuddy.cn/docs/developer-profile 写「实名认证只采集认证所需信息」，对外头像、昵称、简介和联系方式在「设置—开发者信息」填写。

处理原则：

1. 发布计划同时引用企业段和组织段的上限，不合成一条「每账号 10 个主体」；
2. 企业流程中的昵称字段和组织流程中的事后昵称都保留；
3. `developer-profile` 本次不进入来源注册表。

### Buddy 应用：场景数量、背景图、iframe — 2026-10-27

工作模式的两处数量建议仍在：首页配置「建议配置 3–5 个」，最佳实践「建议 2–4 个」。

最佳实践的场景数量已从「至少 5 个高频场景」改为「Top 3–5 高频场景」。

专家页精选场景背景已从 1000×910、底图加 3 层渐变蒙层，改为 792×240、纯色图加右侧插图。

同页两处集成说法：

- 「内嵌已有功能」只写 MCP Apps；
- 「善用已有系统」写 iframe 或 MCP Apps。

处理原则：

1. 工作模式数量继续两处并记，不选一个当唯一官方数字；
2. 场景数量按 Top 3–5 记录；
3. 背景图按 792×240 的新规范准备；
4. iframe 只出现在最佳实践句，不写进「内嵌已有功能」的维度定义。

绑定文案的中文引号改成了 ASCII 引号，模型表单元格多了一个空格（「从 模型池中选择」）。这两处不改变配置要求。

### 技能字段表与示例笔误 — 2026-10-27

中英文技能页的字段表现在把 `name`、`display_name`、`display_name_en` 标为必填，并加入可选的 `examples_zh` / `examples_en`。`disable-model-invocation`、`user-invocable` 和示例里的 `category` 已从两页消失。

官方示例仍是：

- `display_name_en:切英文版展示名称`
- `examples_en` 第二条为 `exmaple 2`

处理原则：

1. 必填集合以当前字段表为准；
2. 模板写正常的 `display_name_en`，不复制缺空格的示例值，也不复制 `exmaple`；
3. 不把已经离开字段表的 `disable-model-invocation` / `user-invocable` 写成运行时已拒绝。当前没有新的平台解析观察。

### 社群入口 — 2026-10-27

三处官方页面现在并不一致：

- 联系渠道页去掉了标题「官方社群」。可见正文只剩咨询邮箱 `openworkbuddy@tencent.com`。相对旧 baseline 少了 105 字节；被删段落的原文没有从 2026-10-09 的公开存档里取回。
- 专家页解析失败段删掉了「，或扫描开放平台首页下方的二维码，加入开发者群聊沟通」。剩下的句子写的是「创建技能过程中」，而这是专家文档。
- 技能页仍写：解析失败可邮件 `openworkbuddy@tencent.com`，或扫描开放平台首页下方的二维码，加入社群沟通。这句相对 2026-10-09 存档没有变化。

处理原则：

1. 对外支持渠道以联系渠道页当前正文为准：邮箱；
2. 不把技能页的二维码句子写回专家页或联系渠道页；
3. 专家页「创建技能」保持为官方笔误，排查步骤仍按专家的基础结构和配置文件。

### 第三方应用权限配置标题 — 2026-10-27

标题从「权限配置列表及关联 API」改为「权限配置」。Scope 行没有增删。权限申请指南新增一句：硬件接入可按业务申请全部 Scope；积分兑换只开放部分权限（例如 `user.credit.exchange`），不提供其他能力域的权限选项。

旧标题里的「关联 API」在 2026-10-09 的正文里并没有对应的 API 列。这次没有新增或删除 Scope 到 API 的映射表。