# Skill Template

这是一个最小 WorkBuddy Skill 起点。

当前必填字段：`name`、`display_name`、`display_name_en`、`description`、`description_zh`、`description_en`、`version`、`author`。模板已有三项名称字段，替换内容时请保留。

可选使用案例为 `examples_zh` / `examples_en` 字符串列表。模板保留的 `user-invocable` / `disable-model-invocation` 是历史配置；2026-10-26 中英文官方页面均未列出，当前平台支持状态需发布前核实，不能由此认定已弃用。

## 使用

1. 修改 `SKILL.md` 的 frontmatter 与正文；
2. 删除或替换 `references/example.md`；
3. 如需 scripts/templates，按实际任务添加；
4. 校验：

```bash
python3 scripts/validate_skill.py path/to/your-skill
```

5. 打包：

```bash
python3 scripts/pack_release.py path/to/your-skill
```

发布前重新核对：https://open.workbuddy.cn/docs/skill
