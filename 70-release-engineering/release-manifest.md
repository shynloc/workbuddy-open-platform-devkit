# Release Manifest

WB-OPDK 为可发布资产定义一个 **DERIVED release manifest**。它不是 WorkBuddy 官方要求上传的文件，而是用于内部可追溯、CI、交接和版本审计。

## 目的

记录：

- 资产类型 / 名称 / 版本
- 生成时间
- 来源 Git commit
- 当时官方来源注册表验证日期
- 每个文件的 SHA256 / 大小
- Validator 状态
- Secret Scan
- Side-effect Review

Schema：

`schemas/release-manifest.schema.json`

## 生成

```bash
python3 scripts/generate_release_manifest.py path/to/asset \
  --validation-status pass \
  --validator scripts/validate_connector.py \
  --side-effect-review pass
```

然后校验：

```bash
python3 scripts/validate_json_schema.py \
  path/to/asset/release-manifest.json \
  schemas/release-manifest.schema.json
```

## 注意

默认 `pack_release.py` 会把目录中现有 manifest 一并打包。如果目标平台不需要该文件，可在发布流程中生成外部 manifest 或在最终包校验时明确排除。

Release Manifest **不能**替代：

- WorkBuddy 官方解析器
- Runtime Test
- Security Review
- 审核结果
