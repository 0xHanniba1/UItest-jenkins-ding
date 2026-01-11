# 项目架构文档

## 系统架构图

```
┌─────────────────────────────────────────────────────────────────────────┐
│                            Jenkins Pipeline                              │
├─────────────────────────────────────────────────────────────────────────┤
│  Checkout ──▶ Install ──▶ Run Tests ──▶ Allure Report ──▶ DingTalk      │
└─────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          测试框架层                                       │
├──────────────────┬──────────────────┬───────────────────────────────────┤
│     pytest       │    Selenium      │         Allure                    │
│   测试运行器      │   浏览器自动化    │        测试报告                    │
└──────────────────┴──────────────────┴───────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          Page Object 层                                  │
├──────────────────────────────┬──────────────────────────────────────────┤
│        BasePage              │           LoginPage                      │
│        页面基类               │          登录页面对象                     │
└──────────────────────────────┴──────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          被测系统 (SUT)                                  │
├──────────────────────────────┬──────────────────────────────────────────┤
│       index.html             │         welcome.html                     │
│        登录页面               │           欢迎页面                        │
└──────────────────────────────┴──────────────────────────────────────────┘
```

## 目录结构

```
UItest-jenkins-ding/
├── config/                     # 配置层
│   ├── __init__.py
│   └── config.py               # 环境配置（URL、浏览器模式）
│
├── pages/                      # Page Object 层
│   ├── __init__.py
│   ├── base_page.py            # 页面基类（通用操作封装）
│   └── login_page.py           # 登录页面对象
│
├── tests/                      # 测试层
│   ├── __init__.py
│   ├── conftest.py             # pytest fixtures（WebDriver）
│   └── test_login.py           # 登录功能测试用例
│
├── test_site/                  # 被测系统
│   ├── index.html              # 模拟登录页面
│   └── welcome.html            # 登录成功页面
│
├── utils/                      # 工具层
│   ├── __init__.py
│   └── dingtalk.py             # 钉钉通知
│
├── docs/                       # 文档
│   ├── spec.md                 # 项目规格
│   ├── architecture.md         # 架构文档（本文件）
│   ├── changelog.md            # 变更日志
│   └── project-status.md       # 项目状态
│
├── reports/                    # 测试报告（gitignore）
├── Jenkinsfile                 # CI/CD Pipeline
├── pytest.ini                  # pytest 配置
├── requirements.txt            # Python 依赖
└── README.md                   # 使用说明
```

## 核心模块说明

### 1. Page Object 模式

```
BasePage (基类)
    ├── find_element()          # 查找元素
    ├── click()                 # 点击
    ├── input_text()            # 输入文本
    ├── get_text()              # 获取文本
    └── wait_for_element()      # 显式等待

LoginPage (登录页面)
    ├── open()                  # 打开登录页
    ├── login(user, pwd)        # 执行登录
    ├── get_error_message()     # 获取错误提示
    └── is_login_successful()   # 判断是否登录成功
```

### 2. 测试配置

```python
# config/config.py
HEADLESS = True/False           # 浏览器模式（环境变量控制）
LOGIN_PAGE_URL = "file://..."   # 测试页面路径
TEST_USER = {"username": "admin", "password": "123456"}
```

### 3. pytest fixtures

```python
# tests/conftest.py
@pytest.fixture
def driver():
    # 初始化 Chrome WebDriver
    # 支持 headless 模式
    # 自动管理 ChromeDriver（webdriver-manager）
    yield driver
    driver.quit()
```

## 数据流

```
1. Jenkins 触发
       │
       ▼
2. pytest 启动测试
       │
       ▼
3. conftest.py 初始化 WebDriver
       │
       ▼
4. test_login.py 执行测试用例
       │
       ▼
5. LoginPage 操作页面元素
       │
       ▼
6. 生成 Allure 报告数据
       │
       ▼
7. Allure 插件生成 HTML 报告
       │
       ▼
8. dingtalk.py 发送通知
```

## 技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| CI/CD | Jenkins | Pipeline 自动化 |
| 测试框架 | pytest | 测试运行、fixtures |
| UI 自动化 | Selenium 4.x | 浏览器操作 |
| 浏览器 | Chrome | 支持 Headless |
| 驱动管理 | webdriver-manager | 自动下载 ChromeDriver |
| 测试报告 | Allure | 可视化报告 |
| 通知 | 钉钉 Webhook | Markdown 消息 |

## 扩展指南

### 添加新页面

1. 在 `pages/` 下创建新页面类，继承 `BasePage`
2. 定义元素定位器和页面操作方法

```python
# pages/new_page.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class NewPage(BasePage):
    ELEMENT = (By.ID, "element-id")

    def do_action(self):
        self.click(self.ELEMENT)
```

### 添加新测试

1. 在 `tests/` 下创建测试文件
2. 使用 `driver` fixture

```python
# tests/test_new_feature.py
from pages.new_page import NewPage

def test_new_feature(driver):
    page = NewPage(driver)
    page.do_action()
    assert page.get_result() == expected
```
