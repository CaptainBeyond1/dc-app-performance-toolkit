import random

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium.webdriver.common.keys import Keys
from selenium_ui.confluence.pages.pages import Login, AllUpdates, Editor
from selenium_ui.confluence.pages.selectors import UrlManager, LoginPageLocators, AllUpdatesLocators, PopupLocators,\
    PageLocators, DashboardLocators, TopPanelLocators, EditorLocators, LogoutLocators
from util.conf import CONFLUENCE_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver);
    if datasets['custom_pages']:
        app_specific_page_id = datasets['custom_page_id']

    @print_timing("selenium_app_custom_action")
    def measure():
        specific_edit_page = Editor(webdriver, page_id=datasets['custom_page_id'])
        specific_edit_page.go_to()
        #Going to editor iframe
        @print_timing("selenium_app_custom_action:copy and paste styles")
        def sub_measure():
            actions = ActionChains(webdriver)
            specific_edit_page = Editor(webdriver, page_id=datasets['custom_page_id'])
            specific_edit_page.wait_until_visible((By.ID, "format-painter-button"))
            specific_edit_page.wait_until_available_to_switch(EditorLocators.page_content_field)
            editor_field = specific_edit_page.get_element((By.ID, "tinymce"))
            editor_field.click()
            #Making sure that everything is loaded and going to tinymce to edit text
            actions.send_keys(Keys.HOME).perform();
            #Going to the beginning of string for easier debugging process
            actions.key_down(Keys.LEFT_SHIFT).send_keys(Keys.ARROW_RIGHT).key_up(Keys.LEFT_SHIFT).perform();
            #Highlighting painted symbol
            specific_edit_page.return_to_parent_frame()
            specific_edit_page.get_element((By.ID, "format-painter-button")).click()
            #Activating format painter
            specific_edit_page.wait_until_available_to_switch(EditorLocators.page_content_field)
            editor_field.click();
            #Going back to content field
            actions.send_keys(Keys.HOME).perform();
            actions.send_keys(Keys.ARROW_RIGHT).perform()

            actions.key_down(Keys.LEFT_SHIFT).perform();
            for x in range(5):
                actions.send_keys(Keys.ARROW_RIGHT).perform()
            actions.key_up(Keys.LEFT_SHIFT).perform();
            actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys("p").key_up(Keys.CONTROL).key_up(Keys.ALT).perform();
            #Highlighting 5 symbols and applying styles via format painter hotkey
        sub_measure()
        specific_edit_page.return_to_parent_frame();
        specific_edit_page.save_edited_page();
    measure()
