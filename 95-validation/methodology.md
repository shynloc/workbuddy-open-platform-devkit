# Real-world Validation Methodology

WB-OPDK 把“本地检查通过”和“WorkBuddy 真实可用”严格分开。

## 五层证据

```text
1. Local Validation
2. Platform Parse
3. Runtime Test
4. Platform Review
5. Published / Production Observation
```

### 1. Local Validation

WB-OPDK Validator / Schema / smoke test 通过。

只能说明：

> 本地结构符合当前知识库规则。

不能说明 WorkBuddy 一定接受。

### 2. Platform Parse

资产成功上传/解析，或 Buddy App 配置被当前开放平台接受。

只能说明：

> 平台当前解析器接受该结构。

不能等同审核通过。

### 3. Runtime Test

在对应 WorkBuddy 客户端实际安装/召唤/连接/运行，并完成关键 Happy/Error/Safety Path。

### 4. Platform Review

记录审核中、驳回、通过，以及平台原始反馈。

审核反馈属于 OBSERVED，不自动升级成 OFFICIAL。

### 5. Published

正式上架/发布后继续观察真实用户环境、升级兼容和依赖变化。

## 记录规则

每个真实验证案例使用一个 YAML：

```text
95-validation/records/<asset-name>-<version>.yaml
```

并通过：

```bash
python3 scripts/validate_validation_records.py
```

校验。

## Evidence

可以记录：

- 截图路径/公开 URL
- GitHub commit
- release manifest
- 平台审核消息（脱敏）
- WorkBuddy 客户端版本
- 测试日志

不要提交：

- Token / Secret
- 私有账号 ID
- 用户隐私
- 未脱敏内部数据
