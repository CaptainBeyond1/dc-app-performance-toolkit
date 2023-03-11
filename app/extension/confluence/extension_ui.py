import random
import uuid
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

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

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out
    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.wait_for_page_loaded()
    #         login_page.set_credentials(username=username, password=password)
    #         login_page.click_login_button()
    #         if login_page.is_first_login():
    #             login_page.first_user_setup()
    #         all_updates_page = AllUpdates(webdriver)
    #         all_updates_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:open_editor_with_macro")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/display/APATDH/1") # Link to a app specific blog, title should match "title ~ 'Selenium*'" CQL, for example "Selenium1"
            page.wait_until_visible((By.ID, "title-text")) # Wait for title field visible
            page.wait_until_visible((By.ID, "editPageLink"))  
            edit_button = page.get_element((By.ID, "editPageLink"))
            edit_button.click()
            page.wait_until_available_to_switch(EditorLocators.page_content_field)
            editor_field = page.get_element((By.ID, "tinymce"))
            page.wait_until_visible((By.CLASS_NAME, "wysiwyg-macro"))
            page.return_to_parent_frame();
            button_publish = page.get_element((By.ID, "rte-button-publish"))
            button_publish.click()
        sub_measure()

        # @print_timing("selenium_app_custom_action:page_to_blog")
        # def sub_measure():
        #     page.wait_until_visible((By.ID, "title-text")) # Wait for converted page title field visible
        #     page.wait_until_visible((By.ID, "action-menu-link")) 
        #     action_menu = page.get_element((By.ID, "action-menu-link"))
        #     action_menu.click()
        #     page.wait_until_visible((By.ID, "page-to-blog-action"))
        #     page_to_blog_action = page.get_element((By.ID, "page-to-blog-action")) # Wait for your app-specific UI element by ID selector
        #     page_to_blog_action.click()
        #     page.wait_until_visible((By.ID, "page-to-blog-dialog"))
        #     page_to_blog_yes = page.get_element((By.ID, "page-to-blog-yes"))
        #     page_to_blog_yes.click()
        #     page.wait_until_invisible((By.ID, "page-to-blog-dialog")) # Wait for the dialog dismissed
        # sub_measure()

        # For this sub measure you need to create a template with "TemplatePageToBlog" title and paste a corresponding macro in it 
        @print_timing("selenium_app_custom_action:create_page_with_macro")
        def sub_measure():
            actions = ActionChains(webdriver)
            page.wait_until_visible((By.ID, "quick-create-page-button"))  # Locate the create page button
            create_page_button = page.get_element((By.ID, "quick-create-page-button"))
            create_page_button.click()
            webdriver.save_screenshot('tinymce.png')
            page.wait_until_visible((By.ID, "rte-button-insert"))  # Wait for teamplates list loaded
            button_insert = page.get_element((By.ID, "rte-button-insert"))
            button_insert.click()
            webdriver.save_screenshot('rte-button-insert.png')
            page.wait_until_visible((By.ID, "rte-insert-macro"))  # Wait for teamplates list loaded
            insert_macro = page.get_element((By.ID, "rte-insert-macro"))
            insert_macro.click()
            actions.send_keys("fx Table").perform() # Search for a app specific template
            webdriver.save_screenshot('fx Table.png')
            page.wait_until_visible((By.ID, "macro-table-formula-macro"))  # Wait for teamplates list loaded
            table_formula_macro = page.get_element((By.ID, "macro-table-formula-macro"))
            table_formula_macro.click()
            page.wait_until_clickable((By.CLASS_NAME, "ok"))
            insert_button = page.get_element((By.CLASS_NAME, "ok"))
            insert_button.click()
            # time.sleep(3)
            # page.wait_until_available_to_switch(EditorLocators.page_content_field)
            # editor_field = page.get_element((By.ID, "tinymce"))
            webdriver.save_screenshot('ok.png')
            page.wait_until_visible((By.ID, "content-title")) 
            content_title = page.get_element((By.ID, "content-title"))
            content_title.click()
            actions.send_keys(uuid.uuid4().hex[:6].upper()).perform()
            webdriver.save_screenshot('title.png')
            # page.return_to_parent_frame();
            button_publish = page.get_element((By.ID, "rte-button-publish"))
            button_publish.click()
            page.wait_until_visible((By.ID, "title-text"))  
        sub_measure()
    measure()
