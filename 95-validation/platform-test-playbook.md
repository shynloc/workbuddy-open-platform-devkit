# WorkBuddy Platform Test Playbook

当一个候选资产已经通过 WB-OPDK Local Validation 后，使用本 Playbook 做真实平台验证。

## 原则

每一步只更新实际发生的状态。

禁止：

- 上传成功就写“审核通过”
- 审核通过就写“Runtime 全通过”
- 一次成功就推断所有版本都兼容
- 把人工观察直接升级为 OFFICIAL

---

# A. Expert — Platform Parse

候选：

`examples/ai-content-editor/`

发布包：

`ai-content-editor-v1.0.0.zip`

## 1. 上传前

确认：

- [ ] 版本 = 1.0.0
- [ ] avatar = 512×512 PNG/JPG，≤500KB
- [ ] plugin.json 与 Agent name 一致
- [ ] 3 tags
- [ ] 3 quick prompts
- [ ] defaultInitPrompt = quickPrompts[0]
- [ ] 本地 Candidate Build 已通过

## 2. Platform Parse

上传 WorkBuddy 开放平台。

记录：

- [ ] ZIP 是否成功解析
- [ ] 是否出现字段级错误
- [ ] 名称/职业/简介/分类/头像是否正确
- [ ] quick prompts 是否正确
- [ ] 是否接受提交审核

如果成功：

```yaml
stages:
  platform_parse:
    status: pass
```

如果失败：

保留平台原始错误文本，写入 evidence / observation。

## 3. Runtime

平台允许实际召唤后，运行：

### Prompt 1

> 把我现在的想法或资料整理成一篇完整可发布的文章。

### Prompt 2

> 检查这篇草稿，帮我优化结构、逻辑和表达。

### Prompt 3

> 把我们刚才的讨论提炼成一个值得写的文章概念和提纲。

观察：

- 角色是否稳定
- 是否保护作者声音
- 是否会无意义跑长流程
- 是否按需要而不是默认研究
- 输出是否符合 Content Editor 定位

---

# B. Expert Team — Platform Parse

候选：

`examples/ai-editorial-team/`

发布包：

`ai-editorial-team-v1.0.0.zip`

## 1. settings.json 已确认

第一次上传使用 `setting.json`（单数）时，WorkBuddy 当前解析器明确失败：

```text
settings.json 不存在或无法读取（Team 型专家必须在 plugin root 下提供 settings.json）
```

修正版候选必须包含：

```text
settings.json
```

内容：

```json
{
  "agent": "ai-editorial-team-team-lead"
}
```

重新上传时重点记录：

- `settings.json` 是否通过文件级解析；
- 如果继续报错，原样记录 JSON 字段/schema 错误；
- 不再测试 `setting.json` 作为有效 fallback。

## 2. Runtime Prompts

### Full Pipeline

> 我有一组关于 AI Agent 工具链的笔记，请团队把它做成一篇完整文章，并给出视觉和发布方案。

期望观察：

```text
Lead
→ Research
→ Writer
→ Art Director
→ Publishing Editor
→ Lead Final QA
```

不要求每次严格线性，但必须看到真实角色分工。

### Draft Review

> 这是我的草稿，让整个编辑部评审并完善，但不要改变我的核心观点。

观察：

- Lead 是否避免所有成员做重复工作
- Writer 是否保护作者观点
- Research 是否只在必要时核查
- Art Director 是否在内容方向稳定后介入

### Research-first

> 先研究 WorkBuddy Connector 的产品化要求，再决定这个题怎么写。

观察：

- Research Editor 是否优先介入
- Writer 是否等待关键事实
- Lead 是否根据研究结果调整任务计划

## 3. Team Failure Tests

至少再测试一次：

- 成员输出存在冲突
- 用户中途改变文章方向
- 只需要“改一个标题”的轻任务

好的 Team 不应该每次都召集全员。

---

# C. 审核状态

平台审核结果出来后：

```text
Pending
→ Approved / Rejected
```

Rejected：

- 保存原始审核反馈
- 做最小必要修复
- 不把一次审核意见自动当作普遍官方规则

Approved：

- 更新 validation record
- 更新 ledger
- 再执行/补齐 Runtime Test
- 如果正式市场可用，再更新 Published

---

# D. 回灌 WB-OPDK

如果实测发现：

- 官方字段差异
- 解析行为变化
- 文档未写明限制
- 模板错误
- Validator 漏检

按影响更新：

```text
sources/known-inconsistencies.md
对应 specification
对应 template
对应 validator/schema
95-validation record
CHANGELOG
```

真实平台行为标记为 OBSERVED，除非官方文档也明确支持。