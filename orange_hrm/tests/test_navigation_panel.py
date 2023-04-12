import pytest

from orange_hrm.pages.navigation_panel import NavigationPanel


@pytest.mark.usefixtures("log_in")
class TestNavigationPanel:

    def test_pages(self):
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()

        navigation_panel.go_to("Admin")
        assert navigation_panel.find_navigated_page(NavigationPanel.PAGE_IS_VISIBLE_ADMIN)
        navigation_panel.go_to("PIM")
        assert navigation_panel.find_navigated_page(NavigationPanel.PAGE_IS_VISIBLE_PIM)
        navigation_panel.go_to("LEAVE")
        assert navigation_panel.find_navigated_page(NavigationPanel.PAGE_IS_VISIBLE_LEAVE)
        navigation_panel.go_to("TIME")
        assert navigation_panel.find_navigated_page(NavigationPanel.PAGE_IS_VISIBLE_TIME)
        navigation_panel.go_to("Recruitment")
        assert navigation_panel.find_navigated_page(NavigationPanel.PAGE_IS_VISIBLE_RECRUITMENT)
        navigation_panel.go_to("My_Info")
        assert navigation_panel.find_navigated_page(NavigationPanel.PAGE_IS_VISIBLE_MY_INFO)
        navigation_panel.go_to("Performance")
        assert navigation_panel.find_navigated_page(NavigationPanel.PAGE_IS_VISIBLE_PERFORMANCE)
        navigation_panel.go_to("Dashboard")
        assert navigation_panel.find_navigated_page(NavigationPanel.PAGE_IS_VISIBLE_DASHBOARD)
        navigation_panel.go_to("Directory")
        assert navigation_panel.find_navigated_page(NavigationPanel.PAGE_IS_VISIBLE_DIRECTORY)
        navigation_panel.go_to("Maintenance")
        navigation_panel.login_maintenance()
        assert navigation_panel.find_navigated_page(NavigationPanel.PAGE_IS_VISIBLE_MAINTENANCE)
        navigation_panel.go_to("Buzz")
        assert navigation_panel.find_navigated_page(NavigationPanel.CONFIRM_MAINTENANCE)
