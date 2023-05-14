import random
import uuid
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates, Editor
from selenium_ui.confluence.pages.selectors import UrlManager, LoginPageLocators, AllUpdatesLocators, PopupLocators,\
    PageLocators, DashboardLocators, TopPanelLocators, EditorLocators, LogoutLocators
from util.conf import CONFLUENCE_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_pages']:
        app_specific_page_id = datasets['custom_page_id']

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:create_page_with_standart_button")
        def sub_measure():
            actions = ActionChains(webdriver)
            page.wait_until_visible((By.ID, "quick-create-page-button"))  # Locate the create page button
            create_page_button = page.get_element((By.ID, "quick-create-page-button"))
            create_page_button.click()
            page.wait_until_visible((By.ID, "rte-button-insert"))  # Wait for teamplates list loaded
            button_insert = page.get_element((By.ID, "rte-button-insert"))
            button_insert.click()
            page.wait_until_visible((By.ID, "rte-insert-macro"))  # Wait for teamplates list loaded
            insert_macro = page.get_element((By.ID, "rte-insert-macro"))
            insert_macro.click()
            actions.send_keys("Page Button (Standard)").perform() # Search for a app specific template
            page.wait_until_visible((By.ID, "macro-pb-page-button"))  # Wait for teamplates list loaded
            macro_page_button = page.get_element((By.ID, "macro-pb-page-button"))
            macro_page_button.click()
            page.wait_until_visible((By.ID, "macro-param-Page"))  # Wait for teamplates list loaded
            page_input = page.get_element((By.ID, "macro-param-Page"))
            page_input.click()
            actions.send_keys("test").perform() # Search for a app specific template
            page.wait_until_visible((By.CLASS_NAME, "content-type-page"))
            actions.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
            page.wait_until_clickable((By.CLASS_NAME, "ok"))
            insert_button = page.get_element((By.CLASS_NAME, "ok"))
            insert_button.click()
            page.wait_until_visible((By.ID, "content-title")) 
            content_title = page.get_element((By.ID, "content-title"))
            content_title.click()
            actions.send_keys(str(uuid.uuid4())).perform()
            # page.return_to_parent_frame();
            button_publish = page.get_element((By.ID, "rte-button-publish"))
            button_publish.click()
            page.wait_until_visible((By.ID, "title-text"))  
        sub_measure()

        @print_timing("selenium_app_custom_action:create_page_with_pulse_button")
        def sub_measure():
            actions = ActionChains(webdriver)
            page.wait_until_visible((By.ID, "quick-create-page-button"))  # Locate the create page button
            create_page_button = page.get_element((By.ID, "quick-create-page-button"))
            create_page_button.click()
            page.wait_until_visible((By.ID, "rte-button-insert"))  # Wait for teamplates list loaded
            button_insert = page.get_element((By.ID, "rte-button-insert"))
            button_insert.click()
            page.wait_until_visible((By.ID, "rte-insert-macro"))  # Wait for teamplates list loaded
            insert_macro = page.get_element((By.ID, "rte-insert-macro"))
            insert_macro.click()
            actions.send_keys("Page Button (Pulse)").perform() # Search for a app specific template
            page.wait_until_visible((By.ID, "macro-pulse-button-v1"))  # Wait for teamplates list loaded
            macro_page_button = page.get_element((By.ID, "macro-pulse-button-v1"))
            macro_page_button.click()
            page.wait_until_visible((By.ID, "macro-param-Page"))  # Wait for teamplates list loaded
            page_input = page.get_element((By.ID, "macro-param-Page"))
            page_input.click()
            actions.send_keys("test").perform() # Search for a app specific template
            page.wait_until_visible((By.CLASS_NAME, "content-type-page"))
            actions.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
            page.wait_until_clickable((By.CLASS_NAME, "ok"))
            insert_button = page.get_element((By.CLASS_NAME, "ok"))
            insert_button.click()
            page.wait_until_visible((By.ID, "content-title")) 
            content_title = page.get_element((By.ID, "content-title"))
            content_title.click()
            actions.send_keys(str(uuid.uuid4())).perform()
            # page.return_to_parent_frame();
            button_publish = page.get_element((By.ID, "rte-button-publish"))
            button_publish.click()
            page.wait_until_visible((By.ID, "title-text"))  
        sub_measure()

    measure()
