---
title: Share Content into WorkBuddy
knowledge_type: OFFICIAL
official_sources:
  - workbuddy-third-party-app
last_verified: 2026-10-20
status: VERIFIED
---

# 分享到 WorkBuddy

官方来源：https://open.workbuddy.cn/docs/third-party-app

2026-10-19 的官方第三方应用页新增「分享能力接入」和「PC端开发手册」。这是一条独立于 OAuth 第三方应用的注册与调用路径：用户从自己的应用把内容分享进 WorkBuddy 的任务输入区。它不使用 `client_id` / `client_secret`，也不出现在 Open API Scope 列表里。

## 边界

官方当前写明：

- 已向通过企业认证的开发者开放。
- 当前支持 PC 端（Windows 应用 / macOS 应用）。移动端（Android / iPhone / 鸿蒙）和分享 SDK 后续开放。
- 用户侧 WorkBuddy 客户端需要 5.8.0 及以上，更低版本无法唤起分享。
- 唤起成功或内容预填成功，不等于用户已经提交任务。
- 场景值当前固定为 `newTask`。输入框里已有内容时，分享内容覆盖当前任务输入区；否则创建新任务并填入输入区。`newTask` 是协议场景名，不表示每次分享都强制创建全新任务。
- 桌面端唤起时不校验发起方应用签名。Windows 代码签名主体/指纹和 macOS Team ID 用于登记、唯一性校验和审核；填错不会导致唤起失败，但会在审核阶段被驳回。

## 注册

入口是开放平台「第三方接入 → 分享功能接入」。按「基础配置 → 应用平台信息」两步填写，可以存草稿。

提交后立即生成应用 ID，状态为「审核中」，此时还不能生成密钥。官方写审核在 7 个工作日内完成；审核期间可以撤回。结果通过开放平台通知中心、WorkBuddy 端内消息中心和开发者邮箱通知。驳回后可修改再提交，应用 ID 不变。通过后状态为「已开通」，到应用详情「安全配置」生成密钥。基础信息提交后固化，后续变更由平台处理；可以新增端。

基础配置里官方标为必填的有：应用名称（全平台唯一；不可使用 Demo / test / 测试等字样）、应用 logo（不小于 96×96px，不大于 100KB，JPG/PNG）、应用简介、应用官网。官网须可正常访问，登录页不算，并需包含应用介绍、功能详情、用户协议、版权和备案信息。申请说明可选。

应用平台信息至少勾选一个端：

| 端 | 官方要求登记的身份 |
|---|---|
| Windows | 主程序可执行文件名或产品名称（不要填反域名包名）、代码签名证书 Subject、40 位十六进制证书指纹（去掉显示用空格）、是否已上架 |
| macOS | Bundle ID、10 位 Team ID、是否已上架 |

开发方式当前固定为 deeplink。应用必须使用企业实名申请的 OV / EV 代码签名证书；自签名或未签名的 Windows 应用无法通过审核。未上架可以接入，把「应用已上架」选为否。

同一端的应用标识与签名信息全平台唯一，只能归属一个主体。名称或标识冲突时，官方给出的申诉邮箱是 `openworkbuddy@tencent.com`。

品牌标识只能用在与分享能力直接相关的入口，并使用官方页所链的 WorkBuddy 品牌中心素材。标识使用不合规范时，平台可以要求整改并暂停分享能力。具体净空、配色和文案限制以官方页当前表格为准，不要从旧截图改写。

## 密钥

密钥在审核通过后由主体超管在浏览器本地生成，创建应用时不提交密钥。官方同时写明：

- 算法材料：RSA-2048，私钥为 PKCS#8 PEM。
- 私钥不经过平台服务端，只在生成弹窗展示一次；平台不保存私钥。
- 生成后展示 `kid`。调用时传入 `kid`，WorkBuddy 用对应公钥验签。
- 生成即生效。同时有效最多 10 对。删除立即生效。
- 轮换方式是先生成新密钥、把签名切到新 `kid`，再删除旧密钥。

同一页对填充方式的两处写法不一致，见 `sources/known-inconsistencies.md`。不要把其中一句改写成唯一官方算法。

## 传输签名包

PC 端 HTTPS 中间页：

```text
https://workbuddy.cn/app/open-deeplink
```

七个查询参数：`appId`、`kid`、`message`、`nonce`、`scene`、`timestamp`、`sig`。用 URL 编码组件编码，不要手工拼接 Base64 里的 `+`、`/`、`=`。签名使用 URL 编码前的字段值。

| 参数 | 官方格式 |
|---|---|
| appId | 开放平台分配的应用标识 |
| kid | 与本次私钥配套的密钥标识 |
| message | 消息对象 UTF-8 JSON 的标准 Base64。原始 JSON 最多 16,384 字节 |
| nonce | 16 字节安全随机数的 32 位小写十六进制 |
| scene | 当前固定 `newTask` |
| timestamp | Unix 秒级十进制字符串，不是毫秒 |
| sig | 待签名串的 RS256 签名，再做标准 Base64。`sig` 自己不进入签名串 |

待签名串按键名 ASCII 顺序拼接，各项之间一个 `&`，末尾不加空格或换行：

```text
appId=Base64(appId)&kid=Base64(kid)&message=<message 的 Base64>&nonce=Base64(nonce)&scene=Base64(scene)&timestamp=Base64(timestamp)
```

`appId`、`kid`、`nonce`、`scene`、`timestamp` 在签名串里是各自值的标准 Base64。`message` 已经是 Base64，签名时不再二次编码。URL 里传输的是原始 `appId`、`kid` 等值，不是签名串里的 `Base64(appId)`。

时效：`-30 <= 平台当前时间 - timestamp <= 300`，单位秒。同一次分享重试保留原包；新分享或包过期后重新生成 `nonce`、`timestamp`、`sig`。同一 `appId + nonce` 最多允许验签成功 3 次。

请在用户发起分享时生成签名包，不要提前生成并长期复用链接。私钥和完整真实分享链接不要放进仓库或问题工单。

## 消息结构

`message` 解码后是 `WorkBuddyMessage`：

| 字段 | 类型 | 官方限制 |
|---|---|---|
| title | string | 不超过 50 字 |
| description | string | 不超过 200 字 |
| payload | TaskPayload | 当前可用任务负载 |

`TaskPayload`：

| 字段 | 类型 | 官方说明 |
|---|---|---|
| action | string | 当前支持 `start` |
| promptContentBlocks | ContentBlock[] | 有顺序，可以混排 |
| connectorIds | string[] | 可选。连接器应已发布，且与分享应用所属主体一致；用户是否已授权仍影响资源读取 |

官方列出的 `ContentBlock.type`：

| type | 已知字段 | 端差异 |
|---|---|---|
| text | `text: string` | |
| image | `data?`、`uri?`、`mimeType?` | 内嵌 `data`：移动端支持，PC 端不支持 |
| audio | `data?`、`uri?`、`mimeType?` | 内嵌 `data`：移动端支持，PC 端不支持 |
| resource | `data?`、`uri?`、`mimeType?` | 内嵌 `data`：移动端支持，PC 端不支持 |
| resource_link | `name?`、`uri`、`_meta?` | 链接需要可访问；可能还需要连接器授权 |

官方明确写：表中的 `?` 只表示不同来源可能不提供该字段，不构成字段组合或必填规则的承诺。字段组合、大小上限和各端完整支持矩阵以正式 SDK / 协议为准。第三方应用能读到的本地 `file://` 路径，WorkBuddy 不一定能读。`_meta` 可以包含 `og:title`、`og:image`、`og:description`。

PC 端不要依赖把图片、音频或文件以 `data` 直接嵌入消息。

## 上线前官方要求核对的失败现象

无法唤起、应用未审核或未启用、接入端身份不符、验签失败、请求过期或 nonce 重放、资源或连接器不可用、内容未预填。官方建议先用纯文本最小消息排除资源问题，并至少覆盖：纯文本 PC 中间页、未安装客户端、错误私钥、过期请求、重复请求、身份不符、不可访问资源。
