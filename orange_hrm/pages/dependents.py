from selenium.webdriver.common.by import By

from selenium.webdriver import Keys

from orange_hrm.pages.personal_details import PersonalDetails


class Dependents(PersonalDetails):

    def __init__(self, driver):
        super().__init__(driver)

    ADD_BUTTON = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--text']")
    RELATIONSHIP_FIELD = (By.CSS_SELECTOR, "div[class='oxd-select-text oxd-select-text--active']")
    RELATIONSHIP_OPTION = (By.CSS_SELECTOR, "div[role ='option']")
    DATE_OF_BIRTH_FIELD = (By.CSS_SELECTOR, "input[placeholder='yyyy-mm-dd']")
    CHECKBOX = (By.CSS_SELECTOR, "i[class= 'oxd-icon bi-check oxd-checkbox-input-icon']")
    DELETE = (By.CSS_SELECTOR,
              "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin']")
    FINALLY_DELETE = (
        By.CSS_SELECTOR,
        "button[class = 'oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")
    EDIT_BUTTON = (By.CSS_SELECTOR, "i[class = 'oxd-icon bi-pencil-fill']")
    NAME = 'Jon'
    TRASH_BUTTON = (By.CSS_SELECTOR, "i[class= 'oxd-icon bi-trash']")
    DEPENDENT_NAME_LIST = (By.CSS_SELECTOR, "div[class ='oxd-table-cell oxd-padding-cell']")

    def click_add_button(self, index):
        add_button_list = self.get_wait().wait_for_list_size_change(self.ADD_BUTTON, 2)
        add_button_list[index].click()

    def add_dependent(self):
        self.click_add_button(0)
        input_fields = self.get_wait().wait_for_list_size_change(PersonalDetails.INPUT_FIELDS, 3)
        self.fill_name(input_fields[1], PersonalDetails.MY_NAME)
        self.get_wait().wait_for_element_to_be_clickable(self.RELATIONSHIP_FIELD).click()
        options = self.get_wait().wait_for_list_size_change(self.RELATIONSHIP_OPTION, 3)
        options[1].click()
        data_of_birth = self.get_wait().wait_for_list_size_change(self.DATE_OF_BIRTH_FIELD, 1)
        self.select_date_of_birth(data_of_birth[0])

    def check_submit(self):
        table = self.get_wait().wait_for_list_size_change(self.DEPENDENT_NAME_LIST, 5)
        return table[1].text == 'Clark'

    def edit_dependent(self):
        self.get_wait().wait_for_element(self.EDIT_BUTTON).click()
        input_fields = self.get_wait().wait_for_list_size_change(PersonalDetails.INPUT_FIELDS, 3)
        input_fields[1].click()
        input_fields[1].send_keys(Keys.CONTROL + 'a')
        input_fields[1].send_keys(Keys.BACK_SPACE)
        self.fill_name(input_fields[1], self.NAME)

    def delete_by_trash(self):
        self.get_wait().wait_for_element(self.TRASH_BUTTON).click()
        self.get_wait().wait_for_element(self.FINALLY_DELETE).click()
        return self.NAME not in self.driver.page_source

    def delete_selected(self):
        checkbox_btn = self.get_wait().wait_for_list_size_change(self.CHECKBOX, 3)
        btn = checkbox_btn[1]
        btn.click()
        self.get_wait().wait_for_element(self.DELETE).click()
        self.get_wait().wait_for_element(self.FINALLY_DELETE).click()
        return PersonalDetails.MY_NAME not in self.driver.page_source
