---
title: WeChat Article Publishing Skill — Real Submission
knowledge_type: OBSERVED
last_verified: 2026-10-08
status: VERIFIED
---

# 微信公众号文章全流程发布 Skill

## Asset

- Display name：微信公众号文章全流程发布
- Internal name：`wechat-article-publishing`
- Version：`1.0.0`
- Type：Skill
- Target：WorkBuddy 技能市场

## 实际工作流

该 Skill 从真实内容生产流程提炼，覆盖：

```text
聊天 / 资料
→ 文章概念
→ Research / Fact Check
→ Draft / Edit
→ Editorial Design
→ Visual Assets
→ WeChat-safe HTML
→ MCP Delivery / Manual Fallback
→ Draft QA
```

WorkBuddy 专版针对官方 Skill 规范进行了适配：

- WorkBuddy frontmatter；
- 中英文 description；
- version / author；
- `@references/...`；
- references / scripts / templates；
- MCP 可用时自动草稿交付；
- 无 MCP 时生成富文本复制 fallback。

## 已实际验证

### Package

- ZIP 根目录结构按 WorkBuddy Skill 格式整理；
- `SKILL.md` 及 references/scripts/templates 能形成完整包；
- 发布版去除了 README/CHANGELOG 等非必要开发文件；
- 临时缓存文件已清理。

### Open Platform

真实执行了：

```text
Skill package
→ WorkBuddy 开放平台上传
→ 图标上传
→ 版本 1.0.0
→ 提交审核
```

平台已接受该资产并进入 **审核中** 状态。

因此当前能够证明：

- 当前 ZIP 基础结构可被开放平台接受；
- 当前元数据没有在提交阶段被拒绝；
- 当前市场 icon 格式满足上传位要求；
- 当前版本成功进入审核工作流。

## 尚不能证明

截至本记录日期：

- 不能声称平台审核已经通过；
- 不能声称已经在公开技能市场可安装；
- 不能把审核中状态当成官方对全部 Skill 规则的确认；
- 尚未用市场安装后的公开版本完成完整 Runtime 回归。

## 后续更新

审核结果出来后更新 Ledger：

```text
Under review
→ Approved / Rejected
→ 如果 Rejected：记录原始审核原因并更新对应 KB
→ 如果 Approved：安装市场版本并跑 Runtime Matrix
→ Published / Runtime Verified
```

如果审核反馈暴露出官方文档未明确的通用规则，应作为 `OBSERVED` 记录，而不是直接改写 `OFFICIAL`。
