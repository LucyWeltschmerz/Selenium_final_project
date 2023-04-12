from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from orange_hrm.base.base_page import BasePage


class EmergencyContacts(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    BUTTONS = (By.CSS_SELECTOR, 'button.oxd-button')
    INPUT_FIELDS = (By.CSS_SELECTOR, 'input.oxd-input')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')
    DATA = (By.CSS_SELECTOR, 'div.data')
    DELETE_BTN = (By.CSS_SELECTOR, 'button.oxd-icon-button')
    CONFIRM_DELETE = (By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm'
                                       '-button-margin')
    FILE_UPLOAD_BTN = (By.CSS_SELECTOR, 'div.oxd-file-button')
    FIlE_UPLOAD = (By.CSS_SELECTOR, "input[type='file']")
    CONTACT_ADDED_ALERT = (By.CSS_SELECTOR, 'div.oxd-toast--success')
    CONTACT_DELETED_ALERT = (By.CSS_SELECTOR, 'div.oxd-toast--success')
    TRASH_BUTTON = (By.CSS_SELECTOR, 'i.oxd-icon.bi-trash')
    EDIT_BUTTON = (By.CSS_SELECTOR, 'i.oxd-icon.bi-pencil-fill')
    CONTACT_TABLE = (By.CSS_SELECTOR, "div[class ='oxd-table-cell oxd-padding-cell']")
    CONTACT_EDITED_ALERT = (By.CSS_SELECTOR, 'div.oxd-toast--success')

    def add_emergency_contact(self):
        buttons = self.get_wait().wait_for_list_size_change(self.BUTTONS, 2)
        add_contact_btn = buttons[0]
        add_contact_btn.click()

    def get_input_fields(self):
        self.get_wait().wait_for_page()
        input_fields = self.get_wait().wait_for_list_size_change(self.INPUT_FIELDS, 6)
        input_field_by_name = ['Search', 'Name', 'Relationship', 'Home_Telephone', 'Mobile', 'Work_Telephone']
        return dict(zip(input_field_by_name, input_fields))

    def go_to_input_field(self, field_name):
        input_field = self.get_input_fields().get(field_name)
        self.get_wait().wait_for_element_to_be_clickable(input_field)
        return input_field

    def fill_input_field(self, field_name, input_text):
        field = self.go_to_input_field(field_name)
        self.get_wait().wait_for_element_to_be_clickable(field).click()
        field.send_keys(Keys.COMMAND + 'a')
        field.send_keys(Keys.BACK_SPACE)
        field.send_keys(input_text)

    def save_emergency_contact(self):
        save_btn = self.wait.wait_for_element_to_be_clickable(self.SUBMIT_BTN)
        save_btn.click()

    def check_for_successfully_added_credential_alert(self):
        return self.get_wait().wait_for_element(self.CONTACT_ADDED_ALERT)

    def check_submitted_information(self, index):
        contact_table = self.get_wait().wait_for_list_size_change(self.CONTACT_TABLE, 7)
        return contact_table[index].text

    def get_contact_data(self, contact_data):
        data_field = self.get_input_fields().get(contact_data)
        return data_field.get_attribute('value')

    def edit_emergency_contact(self, field_name, data):
        self.wait_for_page_load()
        edit_button = self.get_wait().wait_for_element_to_be_clickable(self.EDIT_BUTTON)
        edit_button.click()
        self.fill_input_field(field_name, data)
        self.save_emergency_contact()

    def check_for_successful_edit_credential_alert(self):
        return self.get_wait().wait_for_element(self.CONTACT_EDITED_ALERT)

    def delete_emergency_contact(self):
        self.refresh_page()
        self.wait_for_page_load()
        delete_btn = self.get_wait().wait_for_element_to_be_clickable(self.TRASH_BUTTON)
        delete_btn.click()
        confirm_btn = self.get_wait().wait_for_element_to_be_clickable(self.CONFIRM_DELETE)
        confirm_btn.click()

    def check_for_successfully_deleted_credential_alert(self):
        return self.get_wait().wait_for_element(self.CONTACT_DELETED_ALERT)


