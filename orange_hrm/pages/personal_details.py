from selenium.webdriver.common.by import By

from selenium.webdriver import Keys

from orange_hrm.base.base_page import BasePage


class PersonalDetails(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    NAME = (By.CSS_SELECTOR, "input[name='firstName']")
    MIDDLE_NAME = (By.CSS_SELECTOR, "input[name='middleName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name = 'lastName']")
    MY_NAME = 'Clark'
    MY_MIDDLE_NAME = 'Junior'
    MY_LAST_NAME = "Bush"
    INPUT_FIELDS = (By.CSS_SELECTOR, 'input[class= "oxd-input oxd-input--active"]')
    CALENDAR_MONTH_FIELD = (By.CSS_SELECTOR, 'div[class = "oxd-calendar-selector-month-selected"')
    CALENDAR_MONTH = (By.XPATH, '//li[text() = "January"]')
    CALENDAR_YEAR_FIELD = (By.CSS_SELECTOR, 'div[class = "oxd-calendar-selector-year-selected"]')
    CALENDAR_YEAR = (By.XPATH, '//li[text() = "2020"]')
    CALENDAR_DAY = (By.XPATH, '//div[text() = "20"]')
    NATIONALITY_FIELD = (By.CSS_SELECTOR, ".oxd-select-text")
    NATIONALITIES_LIST = (By.CSS_SELECTOR, "div[class='oxd-select-option']")
    GENDER = (By.XPATH, '(//span[@class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"])[1]')
    SUBMIT = (By.CSS_SELECTOR, "button[type = 'submit']")
    MARTIAL_STATUS_OPTION = (By.XPATH, '//span[text()="Married"]')
    GENERAL = (By.CSS_SELECTOR, 'div[class="oxd-select-text oxd-select-text--active"]')

    def clear_input(self, clear_field):
        element = self.get_wait().wait_for_element(clear_field)
        element.send_keys(Keys.COMMAND + 'a')
        element.send_keys(Keys.BACK_SPACE)

    def fill_name(self, filled_name, fill_field):
        element = self.get_wait().wait_for_element_to_be_clickable(filled_name)
        element.send_keys(fill_field)

    def find_input_fields(self):
        input_fields = self.get_wait().wait_for_list_size_change(self.INPUT_FIELDS, 10)

        fields_inputs = {
            input_fields[0]: 'Nickname',
            input_fields[1]: '1001',
            input_fields[2]: '1002',
            input_fields[3]: '1003',
            input_fields[4]: '1004',
            input_fields[6]: '1006',
            input_fields[7]: '1007',
            input_fields[9]: '1009'
        }
        for key, value in fields_inputs.items():
            key.send_keys(Keys.COMMAND + 'a')
            key.send_keys(Keys.BACK_SPACE)
            key.send_keys(value)

        self.select_date_of_birth(input_fields[8])

    def select_date_of_birth(self, calendar):
        calendar.click()
        self.get_wait().wait_for_element(self.CALENDAR_MONTH_FIELD).click()
        self.get_wait().wait_for_element(self.CALENDAR_MONTH).click()
        self.get_wait().wait_for_element(self.CALENDAR_YEAR_FIELD).click()
        self.get_wait().wait_for_element(self.CALENDAR_YEAR).click()
        self.get_wait().wait_for_element(self.CALENDAR_DAY).click()

    def nationality_checker(self):
        nationality_fild = self.get_wait().wait_for_element_to_be_clickable(self.NATIONALITY_FIELD)
        nationality_fild.click()
        nationalities_list = self.get_wait().wait_for_list_size_change(self.NATIONALITIES_LIST, 193)
        nationalities_list[70].click()

    def radio_button_selection(self):
        gender_field = self.get_wait().wait_for_element(self.GENDER)
        gender_field.click()

    def selection(self, index):
        selection_field = self.get_wait().wait_for_list_size_change(self.GENERAL, 3)
        return selection_field[index]

    def submit(self):
        submit_field = self.get_wait().wait_for_element(self.SUBMIT)
        submit_field.click()

    def assertion(self):
        firstname = self.get_wait().wait_for_element(self.NAME)
        return firstname.get_attribute('value') == self.MY_NAME
