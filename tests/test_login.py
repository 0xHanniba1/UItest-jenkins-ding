import allure
from pages.login_page import LoginPage
from config.config import TEST_USER


@allure.feature("登录功能")
class TestLogin:

    @allure.story("正确登录")
    @allure.title("使用正确的用户名和密码登录成功")
    def test_login_success(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(TEST_USER["username"], TEST_USER["password"])

        assert login_page.is_login_successful(), "登录后应跳转到欢迎页面"
        assert "admin" in login_page.get_welcome_title(), "欢迎页面应显示用户名"

    @allure.story("登录失败")
    @allure.title("使用错误密码登录失败")
    def test_login_wrong_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(TEST_USER["username"], "wrong_password")

        assert not login_page.is_login_successful(), "使用错误密码不应登录成功"
        assert login_page.get_error_message() == "用户名或密码错误"

    @allure.story("登录失败")
    @allure.title("用户名为空时登录失败")
    def test_login_empty_username(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", TEST_USER["password"])

        assert not login_page.is_login_successful(), "用户名为空不应登录成功"
        assert login_page.get_error_message() == "请输入用户名"

    @allure.story("登录失败")
    @allure.title("密码为空时登录失败")
    def test_login_empty_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(TEST_USER["username"], "")

        assert not login_page.is_login_successful(), "密码为空不应登录成功"
        assert login_page.get_error_message() == "请输入密码"
