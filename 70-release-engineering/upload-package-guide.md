---
title: Upload Entry and Release ZIP Guide
knowledge_type: DERIVED
official_sources:
  - workbuddy-skill
  - workbuddy-expert
  - workbuddy-expert-team
last_verified: 2026-10-27
status: VERIFIED
---

# 上传入口与实际 ZIP 验收

先确认目标资产类型与当前页面入口，再选择结构。不要为了消除错误，把原生 Skill 自动转换成专家插件。

## 类型与逻辑根

当前[Skill 官方正文](https://open.workbuddy.cn/docs/skill)、[Expert 官方正文](https://open.workbuddy.cn/docs/expert)及[Expert Team 官方正文](https://open.workbuddy.cn/docs/expert-team)使用不同的资产结构：

| 资产 / 入口 | 逻辑根的关键文件 | 元数据区别 |
|---|---|---|
| 原生 Skill / 技能上传 | `SKILL.md` | YAML frontmatter；author 为字符串；八项必填见下 |
| Expert / 专家配置 | `.codebuddy-plugin/plugin.json`、`agents/`、`avatars/` | 专家 JSON 配置；expertType 为 agent；author 为含 name/email 的对象 |
| Expert Team / 专家团配置 | 专家插件结构，另有 `settings.json` | expertType 为 team；成员/主理人与设置一致 |
| 专家插件内嵌 Skill | `skills/<name>/SKILL.md` | 与插件清单并存，不能代替根清单 |

专家 JSON 的 `skills` 是可选的**相对目录字符串数组**，如 `["./skills/my-skill"]`；`keywords` 也是字符串数组。Agent MD frontmatter 的 `skills` 是预加载名称列表，不能混作插件目录路径。任意 CodeBuddy 插件不自动等于合格的 WorkBuddy 专家包，仍需专家字段、Agent、头像等检查。

原生 Skill 必须有非空字符串 `name`、`display_name`、`display_name_en`、`description`、`description_zh`、`description_en`、`version`、`author`。`examples_zh` / `examples_en` 可省略；提供时本库 Schema 要求字符串数组，如 `examples_zh: ["帮我执行任务"]`。此前宽松 Schema 接受过单个字符串，迁移时应显式改为列表；不能据此推断平台旧包已损坏。插件内嵌 Skill 不自动套用独立市场发布的全部展示字段，本库检查声明目录、`SKILL.md`、YAML 与引用。

## 正确结构示例

DevKit 打包器输出一个资产包装目录，其下就是逻辑根：

```text
my-skill-v1.0.0.zip
└── my-skill/
    ├── SKILL.md
    └── references/
        └── example.md

my-expert-v1.0.0.zip
└── my-expert/
    ├── .codebuddy-plugin/
    │   └── plugin.json
    ├── agents/
    │   └── my-expert.md
    ├── avatars/
    │   └── expert.png
    └── skills/                   # 仅在声明内嵌技能时
        └── helper/
            └── SKILL.md
```

本地 ZIP 验收支持 ZIP 顶层就是逻辑根，或只有一层包装目录；不递归搜索来掩盖额外层级。官方页面展示资产目录，未穷举所有 ZIP 容器布局。上述是本库的可复验静态配置，不保证平台接受所有布局；提交仍需当前平台解析验证。

## 错误结构与定位

| 现象 | 检查与处理 |
|---|---|
| 「配置专家」上传只有原生 SKILL.md 的包，提示未找到插件清单 | 核对目标与入口；不能认定所有 Skill 都必须增加插件清单 |
| `outer/my-expert/.codebuddy-plugin/plugin.json` | 去掉额外导出目录，令逻辑根直接拥有关键文件 |
| 专家包有 agents/、skills/，没有隐藏插件清单 | 检查源文件、ZIP 隐藏目录与额外嵌套；没有原 ZIP 不能区分这些原因 |
| skill.md、Plugin.json、引用大小写不符 | 精确匹配实际条目；本机可读不等于平台可读 |
| 插件 skills 为单字符串，或混用作者对象/字符串 | 按对应官方字段表修正；助手文字不能证明原包实际类型错误 |
| 输出 ZIP 放进源目录 | 打包器拒绝，避免打入自身；使用外部 dist/ |
| 交付 ZIP 与说明/源文件不同 | 对最终交付文件做 --source 比对并记录 SHA256；源修改后重新构建 |

隐藏目录可能被手动通配符或压缩软件漏选。DevKit 使用递归枚举保留 `.codebuddy-plugin` 与 `.mcp.json`，并解包验收；不要删除所有点开头文件。这种风险不表示现有打包器已被证实漏包。

## 可执行流程

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/scaffold.py skill my-skill ./work/my-skill
# 编辑 SKILL.md 和 references，确认主体与资产类型
python3 scripts/release_check.py ./work/my-skill --dist ./dist --side-effect-review not-applicable
python3 scripts/validate_release_zip.py ./dist/my-skill-v1.0.0.zip --type skill --source ./work/my-skill
```

专家用 `scaffold.py expert`，补齐头像和配置后运行发布流程，最终 ZIP 验收用 `--type expert`；团队用 `--type expert-team`，Connector 用 `--type connector`。对应目录校验器不可互换。

`pack_release.py` 验证源配置、生成临时 ZIP、验收归档后才原子替换目标；失败不会交付新的无效 ZIP。`release_check.py` 额外输出 manifest、提交说明和归档 SHA256。manifest 与说明留在 ZIP 外；上传资产 ZIP，不要把整个 dist 再压成一层提交包。

交付前记录 DevKit commit、所选类型/入口、退出码、ZIP 清单、SHA256、是否实际解析和运行。验收读取最终归档，检查结构、Schema、对应规则、声明文件和源内容，不执行业务脚本。声明的嵌套 Agent 同样检查 frontmatter；本地 MCP 声明检查文件和 JSON，团队设置与内嵌 SKILL.md 精确匹配大小写。会被 Windows 改名的尾点、尾空格等条目被拒绝，且解包后的文件名与字节再次对照原 ZIP，避免校验了被覆盖的另一份内容。

## 证据边界

截图可证明页面入口与报错，不能证明 ZIP 内部文件；助手对话不是原 ZIP、真实 manifest 或平台成功证据。保留原 ZIP 与完整错误，先列出条目再决定修复。没有原 ZIP 时应明确根因未定，不宣称原包已修复。

静态通过、真实平台解析、Runtime 与审核是不同证据。本库静态通过不得写成「上传成功」或「平台兼容已保证」。
