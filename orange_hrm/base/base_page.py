from selenium.webdriver import ActionChains

from orange_hrm.base.selenium_driver import SeleniumDriver
from orange_hrm.wait.wait import Wait


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = Wait(self.driver, 30)

    def get_wait(self):
        return self.wait

    def get_actions(self):
        return ActionChains(self.driver)

    def wait_for_page_load(self):
        self.get_wait().wait_for_page()

    def verify_page_title(self, title):
        return self.driver.get_current_page_title() == title

    def verify_page_url(self, url):
        return self.driver.get_current_url() == url

    def verify_get_text(self, text):
        return self.driver.get_text() == text
