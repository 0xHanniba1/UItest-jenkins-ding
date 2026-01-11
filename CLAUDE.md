# UI 自动化 Demo

一句话描述：基于 Selenium + Jenkins 的 UI 自动化测试框架，支持 Allure 报告生成和钉钉通知。

## 项目目标

- 提供模拟登录页面作为测试环境
- 使用 Selenium 实现 UI 自动化测试（支持有头/无头模式切换）
- 集成 Allure 生成可视化测试报告
- Jenkins Pipeline 自动触发测试
- 构建完成后钉钉通知（包含报告链接）

## 技术栈

- 语言：Python 3.9+
- 测试框架：pytest
- UI 自动化：Selenium 4.x
- 浏览器：Chrome（支持 Headless）
- 测试报告：Allure
- CI/CD：Jenkins
- 通知：钉钉 Webhook

## 项目结构

```
ui-automation-demo/
├── docs/
│   └── spec.md
├── test_site/
│   ├── index.html
│   └── welcome.html
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_login.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
├── utils/
│   ├── __init__.py
│   └── dingtalk.py
├── config/
│   └── config.py
├── reports/
├── requirements.txt
├── pytest.ini
├── Jenkinsfile
└── README.md
```

## 开发规范

- 代码风格：PEP 8，使用 black 格式化
- 提交规范：feat/fix/docs/test/refactor 前缀
- 测试要求：新功能必须有对应测试用例
- Page Object 模式：页面元素和操作封装在 pages/ 目录

## 约束条件

- 不要使用 unittest，统一使用 pytest
- 不要硬编码配置，使用环境变量或 config.py
- 不要在代码中明文存储钉钉 Webhook 地址
- 不要提交 reports/ 目录下的文件

## 当前状态

见 [project-status.md](./docs/project-status.md)

## 相关文档

- [项目规格](./docs/spec.md)
- [变更日志](./docs/changelog.md)
