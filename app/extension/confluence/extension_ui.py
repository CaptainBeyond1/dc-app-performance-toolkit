import random
import time
import uuid

from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains
from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS



def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_specific_user_login")
    def measure():
        def app_specific_user_login(username='admin', password='admin'):
            login_page = Login(webdriver)
            login_page.delete_all_cookies()
            login_page.go_to()
            login_page.wait_for_page_loaded()
            login_page.set_credentials(username=username, password=password)
            login_page.click_login_button()
            if login_page.is_first_login():
                login_page.first_user_setup()
            all_updates_page = AllUpdates(webdriver)
            all_updates_page.wait_for_page_loaded()
        app_specific_user_login(username='admin', password='admin')
    measure()

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:blog_to_page")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/display/CT/2023/02/25/SeleniumAppBlog2")
            page.wait_until_visible((By.ID, "title-text"))  # Wait for title field visible
            page.wait_until_visible((By.ID, "action-menu-link"))  # Wait for you app-specific UI element by ID selector
            action_menu = page.get_element((By.ID, "action-menu-link"))
            action_menu.click()
            page.wait_until_visible((By.ID, "blog-to-page-action"))
            blog_to_page_action = page.get_element((By.ID, "blog-to-page-action"))
            blog_to_page_action.click()
            page.wait_until_visible((By.ID, "blog-to-page-dialog"))
            blog_to_page_move = page.get_element((By.ID, "blog-to-page-move"))
            blog_to_page_move.click()
            page.wait_until_invisible((By.ID, "blog-to-page-dialog"))  # Wait for title field invisible
        sub_measure()

        @print_timing("selenium_app_custom_action:page_to_blog")
        def sub_measure():
            page.wait_until_visible((By.ID, "title-text"))  # Wait for title field visible
            page.wait_until_visible((By.ID, "action-menu-link"))  # Wait for you app-specific UI element by ID selector
            action_menu = page.get_element((By.ID, "action-menu-link"))
            action_menu.click()
            page.wait_until_visible((By.ID, "page-to-blog-action"))
            page_to_blog_action = page.get_element((By.ID, "page-to-blog-action"))
            page_to_blog_action.click()
            page.wait_until_visible((By.ID, "page-to-blog-dialog"))
            page_to_blog_yes = page.get_element((By.ID, "page-to-blog-yes"))
            page_to_blog_yes.click()
            page.wait_until_invisible((By.ID, "page-to-blog-dialog"))  # Wait for title field invisible
        sub_measure()

        @print_timing("selenium_app_custom_action:blog_from_template_with_macro")
        def sub_measure():
            actions = ActionChains(webdriver)
            page.wait_until_visible((By.ID, "create-page-button"))  # Wait for title field visible
            create_page_button = page.get_element((By.ID, "create-page-button"))
            create_page_button.click()
            page.wait_until_visible((By.ID, "createDialogFilter"))  # Wait for title field visible
            page.wait_until_invisible((By.CLASS_NAME, "wait-container"))  # Wait for title field visible# Wait for title field visible
            create_dialog_filter = page.get_element((By.ID, "createDialogFilter"))
            create_dialog_filter.click()
            actions.send_keys("TemplatePageToBlog").perform()
            page.wait_until_invisible((By.CLASS_NAME, "wait-container"))  # Wait for title field visible# Wait for title field visible
            create_button = page.get_element((By.CLASS_NAME, "create-dialog-create-button"))
            create_button.click()
            page.wait_until_visible((By.ID, "content-title"))  # Wait for title field visible
            content_title = page.get_element((By.ID, "content-title"))
            content_title.click()
            actions.send_keys(uuid.uuid4().hex[:6].upper()).perform()
            time.sleep(1)
            button_publish = page.get_element((By.ID, "rte-button-publish"))
            button_publish.click()
            page.wait_until_visible((By.ID, "title-text"))  # Wait for title field visible
        sub_measure()
    measure()
