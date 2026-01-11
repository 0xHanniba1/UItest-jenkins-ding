# UI 自动化测试框架

基于 Selenium + Jenkins 的 UI 自动化测试框架，支持 Allure 报告生成和钉钉通知。

## 功能特性

- 模拟登录页面作为测试环境
- Selenium 实现 UI 自动化测试
- 支持有头/无头浏览器模式切换
- Allure 生成可视化测试报告
- Jenkins Pipeline 自动触发测试
- 钉钉 Webhook 推送构建结果

## 项目结构

```
├── config/
│   └── config.py           # 配置文件
├── pages/
│   ├── base_page.py        # Page Object 基类
│   └── login_page.py       # 登录页面对象
├── tests/
│   ├── conftest.py         # pytest fixtures
│   └── test_login.py       # 登录测试用例
├── test_site/
│   ├── index.html          # 模拟登录页面
│   └── welcome.html        # 登录成功页面
├── utils/
│   └── dingtalk.py         # 钉钉通知
├── Jenkinsfile             # Pipeline 配置
├── pytest.ini              # pytest 配置
└── requirements.txt        # Python 依赖
```

## 环境要求

- Python 3.9+
- Chrome 浏览器
- Jenkins（可选，用于 CI/CD）

## 快速开始

### 1. 安装依赖

```bash
pip3 install -r requirements.txt
```

### 2. 运行测试

```bash
# 无头模式（默认）
pytest tests/ -v

# 有头模式（调试）
HEADLESS=false pytest tests/ -v
```

### 3. 生成 Allure 报告

```bash
# 运行测试并生成报告数据
pytest tests/ --alluredir=reports/allure-results

# 查看报告
allure serve reports/allure-results
```

## 测试用例

| 用例 | 描述 | 预期结果 |
|------|------|----------|
| test_login_success | 正确登录 | 跳转欢迎页 |
| test_login_wrong_password | 密码错误 | 提示"用户名或密码错误" |
| test_login_empty_username | 用户名为空 | 提示"请输入用户名" |
| test_login_empty_password | 密码为空 | 提示"请输入密码" |

测试账号：`admin` / `123456`

## Jenkins 配置

### 1. 创建 Pipeline 项目

1. 新建任务 → 选择 "Pipeline"
2. Pipeline → Definition: `Pipeline script from SCM`
3. SCM: `Git`，填写仓库地址
4. Script Path: `Jenkinsfile`

### 2. 配置钉钉通知

1. **Manage Jenkins** → **Credentials**
2. 添加凭据：
   - Kind: `Secret text`
   - ID: `dingtalk-webhook`
   - Secret: 钉钉机器人 Webhook URL

### 3. 触发构建

保存配置后点击 **Build Now**，构建完成后：
- 自动生成 Allure 报告
- 钉钉群收到通知（包含报告链接）

## 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `HEADLESS` | 浏览器模式 | `true` |
| `DINGTALK_WEBHOOK` | 钉钉 Webhook URL | - |

## 本地测试钉钉通知

```bash
DINGTALK_WEBHOOK=https://oapi.dingtalk.com/robot/send?access_token=xxx \
python3 utils/dingtalk.py success
```

## 开发规范

- 代码风格：PEP 8
- 提交前缀：feat/fix/docs/test/refactor
- Page Object 模式封装页面操作

## 相关文档

- [项目规格](./docs/spec.md)
- [变更日志](./docs/changelog.md)
- [项目状态](./docs/project-status.md)
