# Maintenance & Validation Scripts

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

```bash
python3 scripts/validate_skill.py path/to/skill
python3 scripts/validate_expert.py path/to/expert
python3 scripts/validate_expert_team.py path/to/team
python3 scripts/validate_connector.py path/to/connector
python3 scripts/pack_release.py path/to/package --out dist/package.zip
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
