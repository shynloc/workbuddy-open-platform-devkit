---
title: Buddy App Configuration and Release
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-buddy-app
last_verified: 2026-10-07
status: VERIFIED
---

# Buddy App 配置与发布

## 创建应用

官方当前配置包括：

- 应用 ID（自动生成）
- 头像（页面建议 256×256；设计规范另有 16×16 icon 规范，按具体上传位执行）
- 名称
- 简介
- OAuth 授权列表
- 回调 URL
- Trusted Origin

## 首页

- Slogan
- 场景胶囊
- 工作模式
- 内置连接器

官方说明内置连接器需要是支持 OAuth 的 MCP；首次进入并完成 Buddy App 授权后可引导绑定 MCP OAuth。

## 市场

- Experts / Expert Teams
- Skills
- Connectors
- Featured Scenes

## 其他

- 是否跳过首次绑定
- 绑定授权文案
- 输入框占位符（中英文）
- 模型列表、排序、默认模型

## 预览调试

提交审核前必须通过预览链接和对应 WorkBuddy 版本检查配置。

## 发布流程

```text
创建应用
→ 填写基础信息
→ 创建审核通过
→ 分模块配置
→ 预览调试
→ 提交审核
→ 发布上线
```

后续修改需要重新提交审核。
