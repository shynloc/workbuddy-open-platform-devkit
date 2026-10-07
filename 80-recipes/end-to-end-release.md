# Recipe: 从需求到 WorkBuddy 发布包

这条 Recipe 适合 Agent 在用户只给出一个产品想法时，完整推进到“可提交审核”。

## Input

用户可能只说：

> 我有一个 XXX MCP，想上 WorkBuddy。

或：

> 我想做一个专门处理 XXX 的专家。

## Step 1 — 产品类型

读取：

`00-platform/capability-decision-tree.md`

不要先写包。

## Step 2 — Product Brief

使用：

`90-templates/product-brief.md`

明确：

- Target User
- JTBD
- Product Type
- Inputs / Outputs
- Dependencies
- Auth
- Risks
- Release Target
- Definition of Done

## Step 3 — Official Re-check

读取对应官方来源与本地 OFFICIAL 规范。

如果：

- Source Watch 变化；
- 本地标记 STALE；
- 平台 UI 与 KB 不一致；

先核验再开发。

## Step 4 — Scaffold

例如：

```bash
python3 scripts/scaffold.py connector-token my-service ./work/my-service
```

## Step 5 — Build

根据产品类型读取最小上下文，不要一次加载全部仓库。

## Step 6 — Validate

运行对应 Validator + Schema：

```bash
python3 scripts/validate_connector.py ./work/my-service
python3 scripts/validate_schemas.py
```

## Step 7 — Runtime Test

按照：

- `70-release-engineering/test-plan.md`
- `70-release-engineering/runtime-test-matrix.md`
- `70-release-engineering/security-checklist.md`

执行。

## Step 8 — Manifest

```bash
python3 scripts/generate_release_manifest.py ./work/my-service \
  --validation-status pass \
  --validator scripts/validate_connector.py \
  --side-effect-review pass
```

## Step 9 — Package

```bash
python3 scripts/pack_release.py ./work/my-service --out ./dist/my-service-v1.0.0.zip
```

## Step 10 — Submission

用：

`90-templates/submission-checklist.md`

检查：

- 包
- icon/avatar
- 中英文信息
- 示例
- 权限说明
- 审核说明
- 版本号

## Output Contract

Agent 最终应交付：

1. 产品类型判断
2. Product Brief
3. 可发布资产目录
4. Validator 结果
5. Runtime Test 结果
6. Release Manifest
7. ZIP（适用时）
8. 发布资料清单
9. 已知风险 / 未验证点
10. 下一步开放平台操作
