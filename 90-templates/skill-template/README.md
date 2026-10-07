# Skill Template

这是一个最小 WorkBuddy Skill 起点。

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
