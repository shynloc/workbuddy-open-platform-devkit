# Maintenance & Validation Scripts

## Repository Doctor

本地工作级健康检查：

```bash
python3 scripts/doctor.py
python3 scripts/doctor.py --online
python3 scripts/doctor.py --docs
python3 scripts/doctor.py --online --docs
```

或：

```bash
make doctor
```

`--online` 会把当前官方页面与 committed baseline 比较；`--docs` 会额外构建 MkDocs。

## Knowledge base

```bash
python3 scripts/validate_kb.py
python3 scripts/check_official_sources.py
python3 scripts/check_official_sources.py --json
python3 scripts/snapshot_official_sources.py
```

`snapshot_official_sources.py` 只保存 URL、状态、响应头和规范化页面 hash，不镜像官方文档正文。

## Schema validation

先安装开发依赖：

```bash
python3 -m pip install -r requirements-dev.txt
```

然后：

```bash
python3 scripts/validate_schemas.py

python3 scripts/validate_json_schema.py   path/to/instance.json   schemas/connector-meta.schema.json
```

`schemas/` 是 WB-OPDK 的 DERIVED machine-readable schema，不替代 WorkBuddy 官方解析器。

## Release packages

生成 ZIP 或处理上传失败前，先读 `70-release-engineering/upload-package-guide.md`。`pack_release.py` 现在需要 `requirements-dev.txt`，会验证源配置及实际 ZIP 后才替换目标；输出必须在资产目录外。用明确的类型对最终交付文件复验：

```bash
python3 scripts/validate_release_zip.py dist/package.zip --type skill --source path/to/skill
python3 -m unittest discover -s tests -v
```

`--type` 可选值是 skill、expert、expert-team、connector。归档检查接受一个逻辑根（平铺或单层包装），拒绝额外嵌套、错误入口标记、漏掉隐藏清单、声明路径/大小写错误及内容不一致。静态通过不代表真实平台上传成功。

双语报告 v2 的 `missing_in_zh` / `missing_in_en` 表示单侧缺失，`missing_in_both` 单独表示共同缺失；`review_required` 也覆盖共同缺失和大小提示。`--fail-on-mismatch` 对单侧缺失/抓取失败返回 2；需要共同缺失也失败时加 `--fail-on-shared-missing`。监测列表不是平台必填字段表，两个历史调用字段仍接受且状态待核实。

```bash
python3 scripts/validate_skill.py path/to/skill
python3 scripts/validate_expert.py path/to/expert
python3 scripts/validate_expert_team.py path/to/team
python3 scripts/validate_connector.py path/to/connector
python3 scripts/pack_release.py path/to/package --out dist/package.zip
python3 scripts/validate_release_zip.py dist/package.zip --type skill --source path/to/package
```

这些 Validator 是 WB-OPDK 的工程辅助检查，不替代 WorkBuddy 官方解析器和审核。

## Release Manifest

```bash
python3 scripts/generate_release_manifest.py path/to/asset   --validation-status pass   --validator scripts/validate_connector.py   --side-effect-review pass

python3 scripts/validate_json_schema.py   path/to/asset/release-manifest.json   schemas/release-manifest.schema.json
```

Manifest 用于内部版本、审计、CI 和交接；不是 WorkBuddy 官方上传要求。

## Scaffold

```bash
python3 scripts/scaffold.py skill my-skill ./tmp/my-skill
python3 scripts/scaffold.py expert my-expert ./tmp/my-expert
python3 scripts/scaffold.py expert-team my-team ./tmp/my-team
python3 scripts/scaffold.py connector-token my-service ./tmp/my-service
python3 scripts/scaffold.py connector-oauth my-service ./tmp/my-service
python3 scripts/scaffold.py connector-cli my-cli ./tmp/my-cli
python3 scripts/scaffold.py buddy-app my-buddy ./tmp/my-buddy
```

脚手架只负责复制官方适配 starter 与替换基础标识；不会替你生成业务内容，也不会绕过对应 Validator。

## Real-world Validation Records

```bash
python3 scripts/new_validation_record.py \
  --type expert \
  --name my-expert \
  --version 1.0.0

python3 scripts/validate_validation_records.py
```

验证记录用于保存 WorkBuddy 实际 Platform Parse / Runtime / Review / Published 证据，不替代官方规范。

## Submission Notes

```bash
python3 scripts/generate_submission_notes.py path/to/asset \
  --output submission-notes.md
```

只从包内元数据预填确定事实。权限、隐私、外部副作用、审核复现步骤等仍需发布者填写。

`release_check.py` 会自动在 dist/ 中生成同名 `.submission-notes.md`。
