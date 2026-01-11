# 变更日志

## [0.4.0] - 2026-01-11

### 新增
- 钉钉 Webhook 通知功能
  - `utils/dingtalk.py`：钉钉通知脚本
  - 支持 Markdown 格式消息
  - 包含构建状态、项目名、构建号、报告链接
  - 通过 Jenkins 凭据管理 Webhook URL

### 修改
- `Jenkinsfile`：集成钉钉通知，构建成功/失败后自动推送

## [0.3.0] - 2026-01-11

### 新增
- Jenkins Pipeline 配置
  - `Jenkinsfile`：定义 CI/CD 流水线
  - 阶段：Checkout → Install → Test → Report
  - 集成 Allure 插件生成测试报告
  - 支持 headless 模式自动化测试

## [0.2.0] - 2026-01-11

### 新增
- UI 自动化测试框架
  - `config/config.py`：配置文件（URL、headless 模式、测试账号）
  - `pages/base_page.py`：Page Object 基类
  - `pages/login_page.py`：登录页面对象
  - `tests/conftest.py`：pytest fixtures（WebDriver 初始化）
  - `tests/test_login.py`：4 个登录测试用例
  - `requirements.txt`：Python 依赖
  - `pytest.ini`：pytest 配置
- 支持 headless/headed 模式切换（HEADLESS 环境变量）
- 集成 Allure 报告
- 使用 webdriver-manager 自动管理 ChromeDriver

## [0.1.0] - 2026-01-11

### 新增
- 创建模拟登录页面 `test_site/index.html`
  - 用户名、密码输入框
  - 登录按钮
  - 空值校验（用户名为空、密码为空）
  - 凭证校验（admin/123456）
  - 错误提示显示
  - 支持回车键提交
- 创建欢迎页面 `test_site/welcome.html`
  - 登录成功后跳转目标页面
  - 退出登录按钮
