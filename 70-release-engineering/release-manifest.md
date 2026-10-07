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

WB-OPDK 的 `pack_release.py` 默认**排除**资产目录中的 `release-manifest.json`。推荐把 Manifest 输出到 `dist/`，与 ZIP 并列保存：

```text
dist/
├── your-asset-v1.0.0.zip
└── your-asset-v1.0.0.manifest.json
```

这样官方发布包保持纯净，同时内部仍保留可追溯审计记录。

Release Manifest **不能**替代：

- WorkBuddy 官方解析器
- Runtime Test
- Security Review
- 审核结果