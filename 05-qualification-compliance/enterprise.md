---
title: Non-individual Publisher Service Category Notes
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-service-categories-enterprise
last_verified: 2026-10-08
status: VERIFIED
---

# 非个人主体

官方来源：https://open.workbuddy.cn/docs/service-categories-enterprise

非个人主体可覆盖更广的服务场景，但大量高监管类目要求额外资质。

当前官方页面中的典型例子包括：

- 快递收件/派件：可能要求快递业务经营许可证、备案证明或合作协议等；
- 网络小说、视频广场等文娱能力：存在出版、网络文化、视听等资质与额外审核要求；
- 法律服务、公证、电子认证：存在机构许可证/经营范围/授权文件等要求；
- 办公、图片处理、日历、天气、备忘录等工具类目当前存在相对明确的适用边界。

## 工程规则

高监管类产品必须在开发前完成资质确认，不应等到平台审核阶段才发现：

- 主体不符合；
- 许可证缺失；
- 实际功能超出已选类目；
- 公开传播/交易能力触发额外类目。

WB-OPDK 只提供决策流程，不维护一份脱离上游的静态资质清单。
