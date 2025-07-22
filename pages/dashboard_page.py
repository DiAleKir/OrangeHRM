from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

from locators.dashboard_page_locators import DashboardPageLocators


class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE
    locators = DashboardPageLocators



