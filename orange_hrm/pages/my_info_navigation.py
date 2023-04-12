from selenium.webdriver.common.by import By

from orange_hrm.base.base_page import BasePage


class MyInfoNavigation(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    NAVIGATION_TAB = (By.CSS_SELECTOR, "div[role='tab']")

    def go_to_tab(self, tab_name):
        tab_names = ['Personal', 'Contact', 'Emergency', 'Dependents', 'Immigration', 'Job', 'Salary', 'Tax', 'Report',
                     'Qualifications', 'Memberships']
        elements = self.get_wait().wait_for_list_size_change(self.NAVIGATION_TAB, 11)
        tabs = dict(zip(tab_names, elements))
        tabs[tab_name].click()
