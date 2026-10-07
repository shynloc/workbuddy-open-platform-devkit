# v1.0 Real-world Readiness Matrix

WB-OPDK v1.0 的最后门槛不是再增加文档数量，而是用真实 WorkBuddy 环境验证主要资产类型。

## 当前状态

| Asset type | Local schema/validator | Starter smoke test | Platform parse | Runtime test | Review | Published |
|---|---:|---:|---:|---:|---:|---:|
| Skill | ✅ | ✅ | ✅ 1 case | — | ⏳ 1 case | — |
| Expert | ✅ | ✅ | — | — | — | — |
| Expert Team | ✅ | ✅ | — | — | — | — |
| Connector | ✅ | ✅ MCP/CLI | — | — | — | — |
| Buddy App | N/A platform-configured | Product canvas/QA ready | — | — | — | — |
| Third-party App / Open API | OAuth sample syntax ✅ | Integration checklist ✅ | App config not tested | — | — | — |

## 已有真实案例

### Skill

`wechat-article-publishing v1.0.0`

- Local validation: Pass
- Platform parse: Pass
- Review: Pending
- Runtime: Not claimed yet

见：

- `95-validation/records/wechat-article-publishing-1.0.0.yaml`
- `95-validation/wechat-article-publishing-skill.md`

## 本地候选已就绪

### Expert Candidate — AI Content Editor

`examples/ai-content-editor/`

- Schema: Pass
- Expert Validator: Pass
- Release Check: Pass
- Candidate ZIP/manifest/submission-notes: Generated
- Platform Parse: Not run

### Expert Team Candidate — AI Editorial Team

`examples/ai-editorial-team/`

- Schema: Pass
- Team Validator: Pass
- Release Check: Pass
- Candidate ZIP/manifest/submission-notes: Generated
- Platform Parse: Not run
- Special observation target: `setting.json` acceptance

Candidate Build:

https://github.com/shynloc/workbuddy-open-platform-devkit/actions/runs/37669725863

## v1.0 下一批验证顺序

### 1. Expert

目标：

- 使用 WB-OPDK Expert starter 创建一个真实 Expert；
- 通过本地 schema + validator；
- 上传 WorkBuddy；
- 记录 parser 结果；
- 召唤后运行 3 个 quick prompts；
- 记录审核反馈。

建议候选：内容主编 / Editorial Director。

### 2. Expert Team

目标：

- 验证当前 `setting.json` / `settings.json` 上游冲突的真实解析行为；
- 验证 Lead 是否能真实调度至少 2 个 Member；
- 验证 Team Skill / Connector dependency 引导。

建议候选：AI 编辑部。

### 3. Connector

优先选择一个我们能控制服务端、且可安全提供测试账号/Token 的 MCP。

必须验证：

- 首次连接
- 重连
- Token/OAuth 失效
- WorkBuddy 重启后恢复
- Tool schema
- 高风险操作确认
- 多用户凭据隔离

不为了“打勾”直接上架仍是单用户密钥架构的私有 MCP。

### 4. Buddy App

建议候选：Creator Studio。

先验证：

- ≥5 高频场景
- 少量职责清晰 Work Modes
- Skill / Expert / Connector 市场
- 模型排序和默认模型
- Preview link
- 配置审核

### 5. Third-party App / Open API

需要真实 Open Platform App credentials 后验证：

- OAuth authorize / token / refresh
- Local Assistant online/offline
- Cloud Task create/query
- ACP reconnect
- Artifacts REST + SSE recovery

## v1.0 Release Gate

只有满足以下条件才把 WB-OPDK 标为 1.0：

- [ ] Skill 至少 1 个 Published/Approved 真实案例
- [ ] Expert 至少 1 个 Platform Parse + Runtime 案例
- [ ] Expert Team 至少 1 个 Platform Parse + Runtime 案例
- [ ] Connector 至少 1 个真实连接/Runtime 案例
- [ ] Buddy App 至少 1 个 Preview/Review 案例
- [ ] Open API 至少完成一个真实 OAuth + API 调用链
- [ ] 所有重要 OBSERVED 反馈已经回灌 KB/Validator
- [ ] Source Watch、KB CI、HTML Build 持续通过