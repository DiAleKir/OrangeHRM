import allure

from base.base_page import BasePage
from config.links import Links
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE
    locators = LoginPageLocators()

    @allure.step('Enter login')
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.locators.USERNAME_FIELD)).send_keys(login)

    @allure.step('Enter password')
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.locators.PASSWORD_FIELD)).send_keys(password)

    @allure.step('Click submit button')
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SUBMIT_BUTTON)).click()
