---
title: Versioning and Compatibility Operations
knowledge_type: DERIVED
official_sources:
  - workbuddy-open-platform-overview
  - workbuddy-connector
last_verified: 2026-10-08
status: VERIFIED
---

# Versioning & Compatibility

## SemVer

### PATCH

- 文案修正
- 非破坏性 Bug fix
- Validator/模板兼容修复

### MINOR

- 新能力
- 新 Tool
- 新可选配置
- 保持原工作流兼容

### MAJOR

- 删除/重命名核心能力
- 改变用户数据模型
- 改变强依赖/认证方式
- 旧配置无法继续工作

## Compatibility review

每次发布检查：

- 当前 WorkBuddy 官方规范
- `minWorkbuddyVersion`
- upstream template
- Source Watch
- 已知 runtime observations

## Dependency version

外部 MCP/API 发生 breaking change 时：

- 不只升级 Connector；
- 同时检查 Skill、Expert/Team、Buddy App 是否依赖旧 Tool 名/参数。

## Support window

如果要停止支持旧版本，应：

- 提前公告
- 给迁移路径
- 明确最后支持版本
- 保留必要安全修复策略
