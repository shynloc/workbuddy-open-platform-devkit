# Official Template Audit

WorkBuddy 官方 Expert / Expert Team 文档目前提供可下载 ZIP 模板。

WB-OPDK 不直接复制这些 ZIP 到仓库，而是维护：

- 官方下载 URL 注册表：`sources/official-templates.json`
- 已验证 archive/key-file hash：`sources/official-template-audit-baseline.json`
- 审计脚本：`scripts/audit_official_templates.py`
- GitHub Actions：`.github/workflows/template-audit.yml`

## 当前基线（2026-10-08）

### design-experts.zip

Archive SHA256：

`99e14f7096f56c814af2b3369ca2f5184491477721223cc1d60ee2f2f2fc02c3`

关键文件：

- `.codebuddy-plugin/plugin.json`
- `agents/design-md-architect.md`
- `skills/design-reference/SKILL.md`

### trading-team.zip

Archive SHA256：

`4935e7b86b7d32c47d03bb7c70c24adc29a41dc7d74fb9a97596e6d5a3e04345`

关键文件：

- `setting.json`
- `.codebuddy-plugin/plugin.json`
- `agents/trading-team-lead.md`
- `skills/trading-analysis/SKILL.md`

## 变化处理

每月审计 workflow 会下载当前官方 ZIP 并比较 archive hash。

```text
hash 未变化
→ baseline still current

hash 变化
→ workflow fail
→ 上传完整 manifest + safe text files + proposed baseline
→ 人/Agent Review
→ 更新 KB / Schema / Starter / Validator
→ 人工更新 baseline
```

**不会自动覆盖 starter template。**

## 已知发现

官方模板本身可能含 `.DS_Store` / `__MACOSX` 等打包垃圾文件。它们是官方 ZIP 的实际内容，但不是推荐的发布包结构。

WB-OPDK 的 `pack_release.py` 会清理此类文件。
