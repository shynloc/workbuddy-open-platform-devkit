---
title: End-to-end Release Pipeline
knowledge_type: DERIVED
official_sources:
  - workbuddy-open-platform-overview
  - workbuddy-skill
  - workbuddy-expert
  - workbuddy-expert-team
  - workbuddy-connector
  - workbuddy-buddy-app
last_verified: 2026-10-08
status: VERIFIED
---

# End-to-end Release Pipeline

这是一条 WB-OPDK 的统一工程流水线，不是 WorkBuddy 官方要求的唯一流程。

## 0. Official Re-check

提交前重新检查：

- 对应官方产品文档；
- 当前开放平台上传/配置页面；
- `sources/known-inconsistencies.md`；
- Source Watch 是否提示 upstream changed。

## 1. Requirement

输出：

- Product Brief
- Product Type
- Dependencies
- Security / Side-effect gates
- Definition of Done

## 2. Scaffold

```bash
python3 scripts/scaffold.py <type> <name> <output>
```

## 3. Build

按对应目录规范完成：

- Skill → `10-skill/`
- Expert → `20-expert/`
- Expert Team → `30-expert-team/`
- Connector → `40-connector/`
- Buddy App → `50-buddy-app/`
- Third-party App → `60-open-api/`

## 4. Static Validation

```bash
python3 scripts/validate_skill.py ...
python3 scripts/validate_expert.py ...
python3 scripts/validate_expert_team.py ...
python3 scripts/validate_connector.py ...
```

同时运行：

```bash
python3 scripts/validate_schemas.py
```

## 5. Runtime Test

读取：

- `70-release-engineering/test-plan.md`
- `70-release-engineering/runtime-test-matrix.md`
- `70-release-engineering/security-checklist.md`

至少覆盖 Happy Path / Error Path / Auth Expiry / Side Effect / Version Compatibility。

## 6. Release Manifest

```bash
python3 scripts/generate_release_manifest.py path/to/asset \
  --validation-status pass \
  --validator scripts/validate_connector.py \
  --side-effect-review pass
```

Manifest 用于内部版本审计，不是官方强制上传文件。

## 7. Package

```bash
python3 scripts/pack_release.py path/to/package --out dist/release.zip
```

## 8. Submission Materials

读取：

`70-release-engineering/submission-materials.md`

准备：

- 名称/版本/分类/描述
- icon/avatar
- 典型用例
- 权限与认证说明
- 高风险操作说明
- 测试方式

## 9. Platform Review

提交后记录：

- 提交日期
- 包/配置版本
- 审核反馈
- 修复 commit
- 最终通过日期

具有普遍价值的审核反馈写入 OBSERVED，而不是伪装为官方规则。

## 10. Post-release

- 监控版本兼容
- 记录用户反馈
- Source Watch 发现官方变化后重新核验
- SemVer 更新
