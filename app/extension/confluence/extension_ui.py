import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_pages']:
        app_specific_page_id = datasets['custom_page_id']

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:visit_forums_space")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/display/FT")
            page.wait_until_visible((By.ID, "easyForumsTable"))
        sub_measure()

        @print_timing("selenium_app_custom_action:visit_forum")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/display/FT/Forum+1")
            page.wait_until_visible((By.ID, "easyForumsTable"))
        sub_measure()

        @print_timing("selenium_app_custom_action:visit_topic")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/display/FT/Topic+1")
            page.wait_until_visible((By.ID, "title-text"))
        sub_measure()

        @print_timing("selenium_app_custom_action:create_post")
        def sub_measure():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/display/FT/Topic+1")
            page.wait_until_visible((By.ID, "title-text"))
            page.wait_until_visible((By.CLASS_NAME, "quick-comment-prompt"))
            comment_prompt = page.get_element((By.CLASS_NAME, "quick-comment-prompt"))
            comment_prompt.click()
            page.wait_until_visible((By.ID, "wysiwygTextarea_ifr"))
            input_comment = page.get_element((By.ID, "wysiwygTextarea_ifr"))
            input_comment.click()
            input_comment.send_keys('Hey everyone, I just wanted to share a quick update on our project progress. Weve made significant strides in the past week, and Im excited to report that weve successfully completed the first phase of development ahead of schedule!')
            save_button = page.get_element((By.ID, "rte-button-publish"))
            save_button.click()
        sub_measure()
    measure()
