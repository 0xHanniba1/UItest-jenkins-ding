import os
from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent

# 测试页面路径
TEST_SITE_PATH = PROJECT_ROOT / "test_site"
LOGIN_PAGE_URL = f"file://{TEST_SITE_PATH / 'index.html'}"
WELCOME_PAGE_URL = f"file://{TEST_SITE_PATH / 'welcome.html'}"

# 浏览器配置
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
IMPLICIT_WAIT = 10

# 测试账号
TEST_USER = {
    "username": "admin",
    "password": "123456"
}
