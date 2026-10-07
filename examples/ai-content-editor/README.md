# AI Content Editor — Real Validation Candidate

这是 WB-OPDK 为 v1.0 真实平台验证准备的 **Expert 候选资产**。

目标不是把它宣传成已通过 WorkBuddy，而是验证：

1. Expert package 结构；
2. plugin.json 市场字段；
3. 512×512 avatar；
4. Agent frontmatter；
5. WorkBuddy Platform Parse；
6. 实际召唤后的角色稳定性；
7. 3 个 quick prompts；
8. 平台审核。

## 本地检查

在仓库根目录：

```bash
python3 scripts/validate_asset_schemas.py examples/ai-content-editor
python3 scripts/validate_expert.py examples/ai-content-editor
python3 scripts/release_check.py examples/ai-content-editor --dist dist --side-effect-review not-applicable
```

## 平台验证

上传后使用：

```bash
python3 scripts/new_validation_record.py \
  --type expert \
  --name ai-content-editor \
  --version 1.0.0
```

然后只记录真实发生的 Platform Parse / Runtime / Review 状态。
