from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import LOGIN_PAGE_URL


class LoginPage(BasePage):
    # 元素定位器
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.ID, "error-message")
    WELCOME_TITLE = (By.ID, "welcome-title")

    def open(self):
        self.driver.get(LOGIN_PAGE_URL)
        return self

    def enter_username(self, username):
        self.input_text(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password):
        self.input_text(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.click(self.LOGIN_BTN)
        return self

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_successful(self):
        return "welcome.html" in self.get_current_url()

    def get_welcome_title(self):
        self.wait_for_element(self.WELCOME_TITLE)
        return self.get_text(self.WELCOME_TITLE)
