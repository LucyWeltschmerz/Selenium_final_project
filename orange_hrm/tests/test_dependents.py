
import pytest
from orange_hrm.pages.navigation_panel import NavigationPanel
from orange_hrm.pages.dependents import Dependents
from orange_hrm.pages.my_info_navigation import MyInfoNavigation


@pytest.mark.usefixtures("log_in")
class TestDependents:

    def test_dependents(self):
        navigation = NavigationPanel(self.driver)
        navigation.go_to('My_Info')
        my_info_navigation = MyInfoNavigation(self.driver)
        my_info_navigation.wait_for_page_load()
        my_info_navigation.go_to_tab('Dependents')
        dependents = Dependents(self.driver)
        dependents.wait_for_page_load()
        dependents.add_dependent()
        dependents.submit()
        assert dependents.check_submit()
        assert dependents.delete_selected()
        dependents.add_dependent()
        dependents.submit()
        dependents.edit_dependent()
        dependents.submit()
        assert dependents.check_submit()
        assert dependents.delete_by_trash()