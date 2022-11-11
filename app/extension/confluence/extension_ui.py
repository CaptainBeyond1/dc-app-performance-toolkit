import random

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium.webdriver.common.keys import Keys
from selenium_ui.confluence.pages.pages import Login, AllUpdates, Page
from selenium_ui.confluence.pages.selectors import UrlManager, LoginPageLocators, AllUpdatesLocators, PopupLocators, \
    PageLocators, DashboardLocators, TopPanelLocators, EditorLocators, LogoutLocators
from util.conf import CONFLUENCE_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver);
    actions = ActionChains(webdriver)

    @print_timing("selenium_app_custom_action")
    def measure():
        specific_edit_page = Page(webdriver, page_id=datasets['custom_page_id'])
        specific_edit_page.go_to()
        #Going to editor iframe
        @print_timing("selenium_app_custom_action:next_step_click")
        def sub_measure():
            specific_edit_page = Page(webdriver, page_id=datasets['custom_page_id'])
            specific_edit_page.wait_until_visible((By.ID, "navi-next-step"))
            next_step_button = webdriver.find_element_by_id( "navi-next-step")
            actions.move_to_element(next_step_button)
            actions.click()
            actions.perform()
        sub_measure()
        @print_timing("selenium_app_custom_action:next_page_click")
        def sub_measure():
            specific_edit_page.wait_until_visible((By.ID, "navi-next-page"))
            next_step_button = webdriver.find_element_by_id( "navi-next-page")
            actions.move_to_element(next_page_button)
            actions.click()
            actions.perform()
        sub_measure()
    measure()
