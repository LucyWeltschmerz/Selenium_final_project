
import pytest

from orange_hrm.pages.emergency_contacts import EmergencyContacts
from orange_hrm.pages.my_info_navigation import MyInfoNavigation
from orange_hrm.pages.navigation_panel import NavigationPanel


@pytest.mark.usefixtures("log_in")
class TestEmergencyContacts:

    def test_emergency_contacts(self):
        navigation = NavigationPanel(self.driver)
        navigation.go_to('My_Info')
        my_info_navigation = MyInfoNavigation(self.driver)
        my_info_navigation.wait_for_page_load()
        my_info_navigation.go_to_tab('Emergency')
        emergency_contacts = EmergencyContacts(self.driver)
        emergency_contacts.add_emergency_contact()
        emergency_contacts.fill_input_field('Name', 'Arsen')
        emergency_contacts.fill_input_field('Relationship', 'Brother')
        emergency_contacts.fill_input_field('Mobile', '099121212')
        emergency_contacts.save_emergency_contact()
        assert emergency_contacts.check_for_successfully_added_credential_alert()
        emergency_contacts.edit_emergency_contact('Work_Telephone', '099454545')
        assert emergency_contacts.check_for_successful_edit_credential_alert()
        assert emergency_contacts.check_submitted_information(1) == 'Arsen'
        emergency_contacts.delete_emergency_contact()
        assert emergency_contacts.check_for_successfully_deleted_credential_alert()
