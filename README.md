# WB-OPDK — WorkBuddy Open Platform Development Kit

> **一个面向 AI Agent 与开发者的 WorkBuddy 开放平台工程知识库与开发工具包。**  
> 基于 **WorkBuddy 开放平台官方文档** 进行整理、工程化和持续校验；官方文档始终是平台规则的最高可信上游。

[![KB CI](https://github.com/shynloc/workbuddy-open-platform-devkit/actions/workflows/kb-ci.yml/badge.svg)](https://github.com/shynloc/workbuddy-open-platform-devkit/actions/workflows/kb-ci.yml)
[![Source Watch](https://github.com/shynloc/workbuddy-open-platform-devkit/actions/workflows/source-watch.yml/badge.svg)](https://github.com/shynloc/workbuddy-open-platform-devkit/actions/workflows/source-watch.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Source](https://img.shields.io/badge/Upstream-WorkBuddy%20Official-19c37d)](https://open.workbuddy.cn/docs/what-is-open-platform)

## 这是什么？

WB-OPDK（WorkBuddy Open Platform Development Kit）不是 WorkBuddy 官方文档的镜像，也不是官方项目。

它把开放平台规范整理为 **Agent 可快速读取、开发者可直接执行、可以持续追溯和更新** 的工程知识库，覆盖需求判断、架构、开发、测试、打包、审核、发布与版本维护。

```text
WorkBuddy 官方文档
        ↓
   Official Facts
        ↓
工程化解释与决策树
        ↓
SOP / Checklist / Template
        ↓
Skill / Expert / Expert Team / Connector / Buddy App / Open API
        ↓
测试 → 打包 → 审核 → 发布 → 维护
```

## Source of Truth

本项目采用 **Official-first** 原则：

1. **WorkBuddy 当前官方开放平台文档** — 最高可信来源；
2. **开放平台实际 Schema / 后台行为** — 用于发现文档与运行时差异；
3. **本仓库已验证知识** — 对官方规则的工程化整理；
4. **实测记录** — 明确标记为 OBSERVED，不冒充官方规则；
5. **工程建议** — 明确标记为 DERIVED / EXPERIMENTAL。

如果本仓库内容与官方最新文档发生冲突，请以官方文档为准，并提交 Issue / PR 更新本仓库。

### 官方入口

- 开放平台概述：https://open.workbuddy.cn/docs/what-is-open-platform
- 入驻：https://open.workbuddy.cn/docs/onboarding
- Skill：https://open.workbuddy.cn/docs/skill
- 专家：https://open.workbuddy.cn/docs/expert
- 专家团：https://open.workbuddy.cn/docs/expert-team
- 连接器：https://open.workbuddy.cn/docs/connector
- Buddy 应用：https://open.workbuddy.cn/docs/buddy-app
- 第三方应用：https://open.workbuddy.cn/docs/third-party-app
- Open API：https://open.workbuddy.cn/docs/openapi
- 联系渠道：https://open.workbuddy.cn/docs/contact

完整来源注册表见 [`sources/official-sources.yaml`](sources/official-sources.yaml)。

## 当前覆盖

| 模块 | 当前内容 |
|---|---|
| Platform | 产品地图、术语、能力决策树、入驻 |
| Skill | 官方结构、frontmatter、开发 SOP、QA |
| Expert | plugin.json / Agent 规范、设计指南、QA |
| Expert Team | 团队结构、编排、依赖 |
| Connector | MCP / CLI / Auth / 版本兼容 / QA |
| Buddy App | Harness 设计、配置发布、视觉资产、企业分发 |
| Third-party App / Open API | OAuth 2.1、Scope、能力地图 |
| Release Engineering | 需求、包校验、提交资料、审核/版本 |
| Recipes | Skill / Expert / Team / MCP→Connector / Buddy App |
| Templates | Brief、Source Metadata、Release Handoff、Submission QA |
| Maintenance | 官方来源检查脚本、KB metadata validator |

## Quick Start — 开发者

复制对应 Starter，再运行 Validator：

```bash
python3 scripts/validate_skill.py path/to/skill
python3 scripts/validate_expert.py path/to/expert
python3 scripts/validate_expert_team.py path/to/team
python3 scripts/validate_connector.py path/to/connector
python3 scripts/pack_release.py path/to/package --out dist/release.zip
```

模板入口：

- `90-templates/skill-template/`
- `90-templates/expert-template/`
- `90-templates/expert-team-template/`
- `90-templates/connector-mcp-token-template/`
- `90-templates/connector-mcp-oauth-template/`
- `90-templates/connector-cli-template/`
- `90-templates/buddy-app-template/`

CI 会自动执行 KB metadata 校验、Starter smoke test 与 HTML 文档构建。

## 给 AI Agent：从这里开始

**先读 [`START_HERE.md`](START_HERE.md)。**

不要一次性加载整个仓库。先确定产品类型与当前阶段，再按需读取对应目录。

示例：

```text
用户：我有一个微信公众号 MCP，想把它上架 WorkBuddy。

Agent：
1. 读取 START_HERE.md
2. 读取 00-platform/capability-decision-tree.md
3. 判定为 Connector
4. 读取 40-connector/specification.md
5. 按认证形态读取 auth-and-credentials.md
6. 读取 70-release-engineering/
7. 按官方来源核验当前规则
8. 输出需求分析 → 架构 → 开发包 → QA → 发布资料
```

## 先判断你该做什么

```text
可复用 SOP / 方法
    → Skill

固定专业角色
    → Expert

多角色协作
    → Expert Team

外部 API / SaaS / MCP / CLI
    → Connector

完整垂直行业 AI 工作台
    → Buddy App

自己的 App / 网站 / 硬件调用 WorkBuddy
    → Third-party App / Open API
```

更完整的判断逻辑见 [`00-platform/capability-decision-tree.md`](00-platform/capability-decision-tree.md)。

## 知识分类

| 状态 | 含义 |
|---|---|
| `OFFICIAL` | 官方文档明确规定 |
| `DERIVED` | 基于官方规则整理出的工程流程或建议 |
| `OBSERVED` | 实际开发、调试或审核中观察到的行为 |
| `EXPERIMENTAL` | 尚未充分验证的方案 |
| `STALE` | 对应官方来源发生变化，等待重新验证 |
| `DEPRECATED` | 官方已经废弃或不再推荐 |

治理规则见 [`sources/source-policy.md`](sources/source-policy.md)。

## 从需求到发布

```text
Requirement Intake
→ Product Type Decision
→ Product Brief / PRD
→ Architecture
→ Build
→ Local Validation
→ Runtime Test
→ Release Materials
→ Packaging
→ Submission QA
→ Platform Review
→ Review Fix
→ Publish
→ Version & Operations
```

## 目录

```text
├── START_HERE.md
├── 00-platform/
├── 10-skill/
├── 20-expert/
├── 30-expert-team/
├── 40-connector/
├── 50-buddy-app/
├── 60-open-api/
├── 70-release-engineering/
├── 80-recipes/
├── 90-templates/
├── scripts/
└── sources/
```

## 官方来源更新检查

本项目不自动覆盖知识库，只检测变化：

```bash
python3 scripts/check_official_sources.py
python3 scripts/check_official_sources.py --json
python3 scripts/validate_kb.py
```

推荐流程：

```text
检测官方来源 hash 变化
→ 标记相关 KB = STALE
→ 阅读官方 diff
→ 更新文档 / 模板 / Validator
→ 验证
→ 改回 VERIFIED
→ CHANGELOG
```

## 项目边界与声明

- 本项目是非官方、社区性质的开发知识库。
- 本项目基于公开的 WorkBuddy 开放平台官方文档进行归纳、解释与工程化整理。
- 本项目不隶属于、也不代表腾讯或 WorkBuddy 官方。
- WorkBuddy、腾讯及相关名称、商标和产品归其各自权利人所有。
- 涉及平台字段、审核要求、权限、接口或发布规则时，请以官方最新文档与开放平台实际状态为准。

## Contributing

欢迎修正文档过期信息、补充模板/校验器/实战经验，或报告“官方文档 vs 平台行为”的差异。见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## License

MIT License。详见 [`LICENSE`](LICENSE)。