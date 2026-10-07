# DEVELOPER START — 从想法到可提交审核

如果你是人类开发者，先从这里选路径。  
如果你是 AI Agent，请优先读取 [`START_HERE.md`](START_HERE.md)。

## 我只有一个想法，不知道该做什么类型

先读：

1. [产品类型决策树](00-platform/capability-decision-tree.md)
2. [Requirement Intake](70-release-engineering/requirement-intake.md)
3. 复制 [Product Brief](90-templates/product-brief.md)

判断：

```text
SOP / 方法 → Skill
固定专业角色 → Expert
多角色协作 → Expert Team
外部 API / MCP / CLI → Connector
行业工作台 → Buddy App
外部网站/App/硬件调用 WorkBuddy → Third-party App / Open API
```

---

## 我要做 Skill

读：

- [Skill Specification](10-skill/specification.md)
- [Frontmatter](10-skill/frontmatter-reference.md)
- [Development Workflow](10-skill/development-workflow.md)

起项目：

```bash
python3 scripts/scaffold.py skill my-skill ./work/my-skill
```

检查：

```bash
python3 scripts/validate_skill.py ./work/my-skill
python3 scripts/release_check.py ./work/my-skill --dist ./dist --side-effect-review not-applicable
```

---

## 我要做 Expert

读：

- [Expert Specification](20-expert/specification.md)
- [plugin.json Reference](20-expert/plugin-json-reference.md)
- [Expert Design Guide](20-expert/design-guide.md)

起项目：

```bash
python3 scripts/scaffold.py expert my-expert ./work/my-expert
```

补 512×512、≤500KB 的头像后：

```bash
python3 scripts/validate_expert.py ./work/my-expert
```

---

## 我要做 Expert Team

先确认任务真的需要多人角色，不要为了“高级感”强拆 Agent。

读：

- [Team Specification](30-expert-team/specification.md)
- [Orchestration](30-expert-team/orchestration.md)
- [Known Upstream Inconsistencies](sources/known-inconsistencies.md)

起项目：

```bash
python3 scripts/scaffold.py expert-team my-team ./work/my-team
```

---

## 我已经有 MCP，想上 WorkBuddy

读：

- [Connector Specification](40-connector/specification.md)
- [MCP Guide](40-connector/mcp-guide.md)
- [Auth & Credentials](40-connector/auth-and-credentials.md)
- [Version Compatibility](40-connector/version-compatibility.md)

选择：

```bash
# 用户自填 Token / API Key
python3 scripts/scaffold.py connector-token my-service ./work/my-service

# MCP 标准 OAuth
python3 scripts/scaffold.py connector-oauth my-service ./work/my-service
```

如果你的服务已经有成熟 CLI：

```bash
python3 scripts/scaffold.py connector-cli my-cli ./work/my-cli
```

然后：

```bash
python3 scripts/validate_connector.py ./work/my-service
```

---

## 我要做 Buddy App

先不要急着配页面。

读：

- [Buddy App Specification](50-buddy-app/specification.md)
- [Product Design](50-buddy-app/product-design.md)
- [Scenario Design](50-buddy-app/scenario-design.md)

用：

[`90-templates/buddy-app-template/product-canvas.md`](90-templates/buddy-app-template/product-canvas.md)

先定义：

- 目标行业 / 用户
- ≥5 高频场景
- 少量职责明显不同的 Work Modes
- Experts / Skills / Connectors
- 模型策略

再进入开放平台配置与预览。

---

## 我要让自己的产品调用 WorkBuddy

读：

- [Third-party App](60-open-api/third-party-app.md)
- [OAuth 2.1](60-open-api/oauth-2.1.md)
- [Capability Map](60-open-api/capability-map.md)
- [Integration Checklist](60-open-api/integration-checklist.md)

有一个最小 OAuth 示例：

[`examples/third-party-oauth-minimal/`](examples/third-party-oauth-minimal/README.md)

---

## 发布前统一执行

无论什么类型，都读：

- [Runtime Test](70-release-engineering/runtime-test-matrix.md)
- [Security Checklist](70-release-engineering/security-checklist.md)
- [Submission Materials](70-release-engineering/submission-materials.md)
- [End-to-end Release Pipeline](70-release-engineering/release-pipeline.md)

可打包资产最终建议：

```bash
python3 scripts/release_check.py ./work/your-asset --dist ./dist
```

最终仍必须经过：

```text
WB-OPDK static checks
→ WorkBuddy real parser
→ Runtime Test
→ Platform Review
```

本 DevKit 不声称替代 WorkBuddy 官方解析器或审核。
