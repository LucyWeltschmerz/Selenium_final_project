import pytest

from orange_hrm.pages.contact_details import ContactDetails
from orange_hrm.pages.my_info_navigation import MyInfoNavigation
from orange_hrm.pages.navigation_panel import NavigationPanel


@pytest.mark.usefixtures("log_in")
class TestContactDetails:

    def test_contact_details(self):
        navigation = NavigationPanel(self.driver)
        navigation.go_to('My_Info')
        my_info_navigation = MyInfoNavigation(self.driver)
        my_info_navigation.wait_for_page_load()
        my_info_navigation.go_to_tab('Contact')
        contact_details = ContactDetails(self.driver)
        contact_details.wait_for_page_load()
        contact_details.fill_input('Street_one', 'Gago')
        contact_details.fill_input('City', 'Vazgen')
        contact_details.fill_input('State', 'Utah')
        contact_details.fill_input('Zip', '123')
        contact_details.select_country('Albania')
        contact_details.save_button_click()
        contact_details.wait_for_save()
        assert contact_details.get_input_text('State') == 'Utah'
        assert contact_details.get_input_text('Zip') == '123'
        assert contact_details.get_input_text('City') == 'Vazgen'
        assert contact_details.get_input_text('Street_one') == 'Gago'
        assert contact_details.get_input_text('Zip') == '123'
        assert contact_details.get_country() == 'Albania'
