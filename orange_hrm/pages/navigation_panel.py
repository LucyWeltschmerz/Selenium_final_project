from selenium.webdriver.common.by import By

from orange_hrm.base.base_page import BasePage


class NavigationPanel(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    ROOT_ELEMENT = (By.CSS_SELECTOR, 'nav[aria-label="Sidepanel"]')
    NAVIGATION_ITEMS = (By.CSS_SELECTOR, 'ul[class=oxd-main-menu] > li')
    PAGE_IS_VISIBLE_RECRUITMENT = (By.CSS_SELECTOR, 'li[class = "oxd-topbar-body-nav-tab --visited"]')
    PAGE_IS_VISIBLE_ADMIN = (By.CSS_SELECTOR, 'h5[class = "oxd-text oxd-text--h5 oxd-table-filter-title"]')
    PAGE_IS_VISIBLE_PIM = (By.CSS_SELECTOR, 'li[class = "oxd-topbar-body-nav-tab --parent"]')
    PAGE_IS_VISIBLE_LEAVE = (By.CSS_SELECTOR, 'h5[class = "oxd-text oxd-text--h5 oxd-table-filter-title"]')
    PAGE_IS_VISIBLE_TIME = (By.CSS_SELECTOR, 'div[class = "oxd-topbar-header-title"]')
    PAGE_IS_VISIBLE_MY_INFO = (By.CSS_SELECTOR, 'a[class= "orangehrm-tabs-item --active"]')
    PAGE_IS_VISIBLE_PERFORMANCE = (By.CSS_SELECTOR, 'a[class = "oxd-topbar-body-nav-tab-item"]')
    PAGE_IS_VISIBLE_DASHBOARD = (By.CSS_SELECTOR, 'div[class = "oxd-grid-3 orangehrm-dashboard-grid"')
    PAGE_IS_VISIBLE_DIRECTORY = (By.CSS_SELECTOR, 'h5[class = "oxd-text oxd-text--h5 oxd-table-filter-title"]')
    PAGE_IS_VISIBLE_MAINTENANCE = (By.CSS_SELECTOR, 'h6[class = "oxd-text oxd-text--h6 orangehrm-main-title"]')
    LOGIN_MAINTENANCE = (By.CSS_SELECTOR, 'input[type = "password"]')
    CONFIRM_MAINTENANCE = (By.CSS_SELECTOR, 'button[type = "submit"]')

    def get_navigation_items(self):
        self.get_wait().wait_for_page()
        navigation_elements = self.get_wait().wait_for_list_size_change(self.NAVIGATION_ITEMS, size=11)
        navigation_item_names = ['Admin', 'PIM', 'LEAVE', 'TIME', 'Recruitment', 'My_Info', 'Performance', 'Dashboard',
                                 'Directory', 'Maintenance', 'Buzz']
        return dict(zip(navigation_item_names, navigation_elements))

    def go_to(self, page):
        element = self.get_navigation_items().get(page)
        self.get_wait().wait_for_element_to_be_clickable(element)
        self.click(element)

    def find_navigated_page(self, locator):
        return self.get_wait().wait_for_element(locator)

    def login_maintenance(self):
        element = self.get_wait().wait_for_element(self.LOGIN_MAINTENANCE)
        element.send_keys('admin123')
        self.find_element_by(self.CONFIRM_MAINTENANCE).click()
