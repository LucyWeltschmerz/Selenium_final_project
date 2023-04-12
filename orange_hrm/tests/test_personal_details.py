import pytest

from orange_hrm.pages.navigation_panel import NavigationPanel
from orange_hrm.pages.personal_details import PersonalDetails


@pytest.mark.usefixtures("log_in")
class TestPersonalDetails:

    def test_personal_details(self):
        navigation = NavigationPanel(self.driver)
        navigation.go_to('My_Info')
        personal_details_page = PersonalDetails(self.driver)
        personal_details_page.wait_for_page_load()
        personal_details_page.clear_input(PersonalDetails.NAME)
        personal_details_page.fill_name(PersonalDetails.NAME, PersonalDetails.MY_NAME)
        personal_details_page.clear_input(PersonalDetails.MIDDLE_NAME)
        personal_details_page.fill_name(PersonalDetails.MIDDLE_NAME, PersonalDetails.MY_MIDDLE_NAME)
        personal_details_page.clear_input(PersonalDetails.LAST_NAME)
        personal_details_page.fill_name(PersonalDetails.LAST_NAME, PersonalDetails.MY_LAST_NAME)
        personal_details_page.find_input_fields()
        personal_details_page.nationality_checker()
        personal_details_page.radio_button_selection()
        personal_details_page.submit()
        assert personal_details_page.assertion()
