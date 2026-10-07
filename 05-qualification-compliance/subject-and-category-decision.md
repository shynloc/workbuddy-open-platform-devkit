---
title: Publisher Entity and Service Category Decision
knowledge_type: DERIVED
official_sources:
  - workbuddy-onboarding
  - workbuddy-service-categories-individual
  - workbuddy-service-categories-enterprise
last_verified: 2026-10-08
status: VERIFIED
---

# 主体与服务类目决策

## 1. 先确定发布主体

- 个人主体
- 非个人主体（企业/组织等）

主体身份不是“市场展示字段”，它会影响可选服务类目和资质要求。

## 2. 按实际功能判断服务

不要按产品名字选类目，要按用户实际能做什么判断。

例如：

- 只是信息展示 ≠ 在线交易
- 本地图片处理 ≠ 公开内容社区
- 教育信息展示 ≠ 视频课程销售/直播
- 查件 ≠ 寄件/收件
- 健康记录 ≠ 医疗诊疗

## 3. 查官方类目

个人主体：

https://open.workbuddy.cn/docs/service-categories-individual

非个人主体：

https://open.workbuddy.cn/docs/service-categories-enterprise

## 4. 资质 Gate

如果类目要求许可证/执业证/备案/合作协议：

```text
Have required qualification?
├── Yes → continue
└── No
    ├── change product scope
    ├── change publisher entity
    └── stop submission
```

不要通过改文案掩盖实际服务能力。

## 5. Product Brief 必须记录

- Publisher entity
- Intended service category
- Actual user-facing service
- Qualification required
- Qualification evidence owner
- Last official category check date
