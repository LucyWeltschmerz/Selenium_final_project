import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from orange_hrm.base.base_page import BasePage


class ContactDetails(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    FORM = (By.CSS_SELECTOR, 'form[class="oxd-form"] ')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[class$= orangehrm-left-space]')
    INPUTS = (By.CSS_SELECTOR, 'input[class*=oxd-input]')
    COUNTRY_SELECT = (By.CSS_SELECTOR, 'div[class=oxd-select-wrapper]')
    LOADING_SPINNER = (By.CSS_SELECTOR, 'div[class=oxd-loading-spinner')

    def get_input_by_name(self, input_name):
        input_names = ['Street_one', 'Street_second', 'City', 'State', 'Zip', 'Home_Phone', 'Mobile_Phone',
                       'Work_Phone', 'Work_Email', 'Other_Email']

        form = self.get_wait().wait_for_element(self.FORM)

        elements = form.find_elements(*self.INPUTS)
        inputs = dict(zip(input_names, elements))
        return inputs[input_name]

    def select_country(self, country_name):
        self.find_element_by(self.COUNTRY_SELECT).click()
        self.get_wait().wait_for_element_to_be_clickable((By.XPATH, f"//*[text()='{country_name}']")).click()

    def fill_input(self, input_name, input_text, is_last=False):
        element = self.get_input_by_name(input_name)
        self.get_wait().wait_for_element_to_be_clickable(element).click()
        element.send_keys(Keys.COMMAND + 'a')
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(input_text)
        if is_last:
            element.send_keys(Keys.ENTER)

    def get_input_text(self, input_name):
        element = self.get_input_by_name(input_name)
        return element.get_attribute('value')

    def get_country(self):
        return self.find_element_by(self.COUNTRY_SELECT).text

    def save_button_click(self):
        self.driver.execute_script('window.scrollTo(0, 500)')
        el = self.find_element_by(self.SAVE_BUTTON)
        time.sleep(1)
        self.get_wait().wait_for_element_to_be_clickable(el).click()

    def wait_for_save(self):
        self.get_wait().wait_for_element(self.LOADING_SPINNER)
        self.get_wait().wait_for_element(self.INPUTS)
