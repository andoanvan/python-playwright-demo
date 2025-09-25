import allure
from playwright.sync_api import Page

from configs.configs import Configs
from core.page.base_page import BasePage
from pages.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Navigate to {url}")
    def goto(self, url: str):
        super().goto(url)

    @allure.step("Perform login")
    def login(self):
        self.fill_username(Configs.get().AUTH_USERNAME)
        self.fill_password(Configs.get().AUTH_PASSWORD)
        self.click_login_button()
        return self

    @allure.step("Fill username with {username}")
    def fill_username(self, username: str):
        self.fill_input(LoginPageLocators.USERNAME_TXT, username)
        return self

    @allure.step("Fill password with {password}")
    def fill_password(self, password: str):
        self.fill_input(LoginPageLocators.PASSWORD_TXT, password)
        return self

    @allure.step("Click login button")
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BTN)
        return self
