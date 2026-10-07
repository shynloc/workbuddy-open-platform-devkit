# Skill QA Checklist

## Structure

- [ ] 根目录名稳定、建议 kebab-case
- [ ] `SKILL.md` 存在
- [ ] references/scripts/templates 仅在需要时提供
- [ ] ZIP 中不额外嵌套一层无意义目录

## Frontmatter

- [ ] description
- [ ] description_zh
- [ ] description_en
- [ ] version
- [ ] author
- [ ] description 清楚写用途/触发场景
- [ ] allowed-tools 如填写，确实是必要限制
- [ ] user-invocable / disable-model-invocation 与产品意图一致

## References

- [ ] 所有 `@references/...` 都存在
- [ ] 引用只加载需要的上下文
- [ ] 关键外部规范有来源和验证日期

## Scripts

- [ ] Bash 可调用
- [ ] 参数写清
- [ ] 错误码/错误信息可理解
- [ ] 不写死用户路径/Secret
- [ ] 无脚本环境时有可行 fallback（若业务允许）

## Behavior

- [ ] 能从用户自然语言触发
- [ ] 不把一次性任务过度包装成 Skill
- [ ] Definition of Done 可验证
- [ ] 高风险操作有显式确认
