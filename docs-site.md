# HTML Knowledge Base

WB-OPDK 使用 Markdown 作为唯一知识源，通过 MkDocs 构建静态 HTML。

## 本地构建

```bash
python3 -m pip install -r requirements-docs.txt
mkdocs serve
```

构建静态站：

```bash
mkdocs build
```

默认输出到仓库上级目录的 `wb-opdk-site/`。

## CI

`.github/workflows/kb-ci.yml` 会：

1. 验证 KB metadata；
2. 构建 HTML；
3. 将构建站点作为 GitHub Actions artifact 上传。

当前不自动部署 GitHub Pages。需要公开文档站时再启用 Pages，避免在内容仍快速迭代时产生第二个“看起来像官方”的公开入口。

## Official Source Watch

`.github/workflows/source-watch.yml` 每周抓取 `sources/official-sources.yaml` 中的官方 URL 并生成状态/hash artifact。

它只检测，不自动改写本地知识库。

正确流程：

```text
检测变化
→ 人/Agent 看 diff
→ 标记受影响文档 STALE
→ 更新知识/模板/校验器
→ 再验证
→ VERIFIED
```
