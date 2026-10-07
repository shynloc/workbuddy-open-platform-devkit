# START HERE — Agent Entry Point

> AI Agent 进入 WB-OPDK 时先读本文件。

## 0. Source of Truth

规则优先级：

1. WorkBuddy 当前官方开放平台文档
2. 官方开放平台实际 Schema / 后台行为
3. 本知识库 VERIFIED 内容
4. OBSERVED 实测
5. DERIVED / EXPERIMENTAL 工程建议

如果本地文档标记为 `STALE`、平台报未知字段/解析错误、或用户反馈与 KB 不一致：**先回查官方来源，不要猜。**

来源注册表：`sources/official-sources.yaml`  
治理规则：`sources/source-policy.md`  
已知官方冲突：`sources/known-inconsistencies.md`

## 1. 先做发布主体 / 资质 Gate

如果任务目标包含“上架、发布、审核”：

1. 读取 `05-qualification-compliance/subject-and-category-decision.md`
2. 确认个人 / 非个人主体
3. 按真实服务核对官方服务类目
4. 如果需要额外资质，先确认资质再开发

然后再判断产品类型。

## 2. 判断产品类型

读取：`00-platform/capability-decision-tree.md`

- SOP / 方法 → Skill
- 固定专业角色 → Expert
- 多角色真实协作 → Expert Team
- 外部 API / MCP / CLI → Connector
- 垂直行业工作台 → Buddy App
- 外部 App / 网站 / 硬件调用 WorkBuddy → Third-party App / Open API

## 3. 按类型最小加载

### Skill

1. `10-skill/specification.md`
2. 字段 → `10-skill/frontmatter-reference.md`
3. `10-skill/development-workflow.md`
4. `10-skill/qa-checklist.md`

### Expert

1. `20-expert/specification.md`
2. 分类 → `20-expert/category-reference.md`
3. `20-expert/design-guide.md`
4. `20-expert/qa-checklist.md`

### Expert Team

1. `30-expert-team/specification.md`
2. `30-expert-team/orchestration.md`
3. settings → `30-expert-team/settings-json.md`
4. 如需外部能力：`30-expert-team/dependencies.md`

### Connector

1. `40-connector/specification.md`
2. MCP → `40-connector/mcp-guide.md`
3. CLI → `40-connector/cli-guide.md`
4. 认证 → `40-connector/auth-and-credentials.md`
5. 新字段 → `40-connector/version-compatibility.md`
6. `40-connector/qa-checklist.md`

### Buddy App

1. `50-buddy-app/specification.md`
2. `50-buddy-app/product-design.md`
3. `50-buddy-app/configuration-and-release.md`
4. 视觉 → `50-buddy-app/design-assets.md`
5. B2B → `50-buddy-app/enterprise-distribution.md`

### Hardware

1. `55-hardware/README.md`
2. `55-hardware/architecture.md`
3. `55-hardware/oauth-and-scopes.md`
4. `55-hardware/runtime.md`
5. `55-hardware/device-security.md`

### Third-party App / Open API

1. `60-open-api/third-party-app.md`
2. `60-open-api/oauth-2.1.md`
3. 快速索引 → `60-open-api/endpoints-quick-reference.md`
4. Local Assistant → `60-open-api/local-assistant.md`
5. Cloud Task → `60-open-api/cloud-tasks.md`
6. ACP / Artifacts → `60-open-api/acp-and-artifacts.md`

## 4. 共用 Security & Release Engineering

涉及用户数据、外部账户、写操作或 Open API 时先读取 `65-security-governance/`。

开发中后期读取 `70-release-engineering/`：

需求 → 开发 → QA → Runtime Test → Security Review → 发布资料 → 审核 → 版本维护

重点：

- `runtime-test-matrix.md`
- `security-checklist.md`
- `package-validation.md`
- `submission-materials.md`

## 5. 可直接使用的模板

`90-templates/` 当前包含：

- Skill starter
- Expert starter
- MCP + Token Connector starter
- Product Brief
- Release Handoff
- Submission Checklist

## 6. Validator / Packaging

```bash
python3 scripts/validate_skill.py <skill-root>
python3 scripts/validate_expert.py <expert-root>
python3 scripts/validate_expert_team.py <team-root>
python3 scripts/validate_connector.py <connector-root>
python3 scripts/pack_release.py <asset-root>
```

这些脚本是辅助校验，不替代 WorkBuddy 开放平台最终解析结果。

## 7. 上线后运营

正式发布后读取 `75-operations/`：

- post-release
- versioning & compatibility
- rollback & incident
- deprecation
- support handoff

## 8. Agent 工作纪律

- 不一次性加载整个仓库；
- 字段不得凭记忆杜撰；
- OFFICIAL 与 DERIVED/OBSERVED 必须区分；
- 当前官方来源不支持的点要明确说“未确认”；
- 官方内部存在冲突时不要静默选边；
- 不把 Secret/Token/AppSecret 写进公开仓库；
- 有外部副作用的动作设计明确确认门槛；
- 发布前重新核验官方文档与当前开放平台界面。