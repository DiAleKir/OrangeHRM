import allure

from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f'Open {self.PAGE_URL} page'):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f'Page {self.PAGE_URL} is opened'):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    @allure.step('Click on "Admin" link')
    def click_admin_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.ADMIN_LINK)).click()

    @allure.step('Click on "PIM" link')
    def click_pim_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.PIM_LINK)).click()

    @allure.step('Click on "Leave" link')
    def click_leave_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.LEAVE_LINK)).click()

    @allure.step('Click on "Time" link')
    def click_time_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.TIME_LINK)).click()

    @allure.step('Click on "Recruitment" link')
    def click_recruitment_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.RECRUITMENT_LINK)).click()

    @allure.step('Click on "My Info" link')
    def click_my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.MY_INFO_LINK)).click()

    @allure.step('Click on "Performance" link')
    def click_performance_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.PERFORMANCE_LINK)).click()

    @allure.step('Click on "My Info" link')
    def click_dashboard_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.DASHBOARD_LINK)).click()

    @allure.step('Click on "Directory" link')
    def click_directory_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.DIRECTORY_LINK)).click()

    @allure.step('Click on "Maintenance" link')
    def click_maintenance_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.MAINTENANCE_LINK)).click()

    @allure.step('Click on "Claim" link')
    def click_claim_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.CLAIM_LINK)).click()

    @allure.step('Click on "Buzz" link')
    def click_buzz_link(self):
        self.wait.until(EC.element_to_be_clickable(BaseLocators.BUZZ_LINK)).click()

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )