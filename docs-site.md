# HTML Knowledge Base

WB-OPDK 使用 Markdown 作为唯一知识源，通过 MkDocs 构建静态 HTML。

为了保持根目录对 AI Agent 友好，知识源不迁移到传统 `docs/`。构建前由 `scripts/prepare_docs.py` 把需要的内容复制到 `build/docs/`，MkDocs 再输出到 `build/site/`。

## 本地预览

```bash
python3 scripts/prepare_docs.py
python3 -m pip install -r requirements-docs.txt
mkdocs serve
```

## 构建静态站

```bash
python3 scripts/prepare_docs.py
mkdocs build
```

输出：

```text
build/site/
```

整个 `build/` 已被 gitignore，不会污染知识源。

## CI

`.github/workflows/kb-ci.yml` 会：

1. 验证 KB metadata；
2. smoke-test starter templates；
3. 生成 `build/docs/`；
4. 构建 HTML；
5. 把 `build/site/` 作为 GitHub Actions artifact 上传。

当前不自动部署 GitHub Pages。等内容和导航稳定后，再决定是否启用公开文档站。

## Official Source Watch

`.github/workflows/source-watch.yml` 会定期检查 `sources/official-sources.yaml`：

- 获取官方页面；
- 计算 visible-text / HTML hash；
- 有 baseline 时比较变化；
- 生成 proposed baseline artifact；
- **不会自动修改任何 KB 文档**。

正确流程：

```text
检测变化
→ 人/Agent 看 diff
→ 标记受影响文档 STALE
→ 更新知识/模板/校验器
→ 再验证
→ VERIFIED
```
