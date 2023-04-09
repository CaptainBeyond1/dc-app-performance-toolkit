import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_instantsearch")
    def measure():

        @print_timing("selenium_instantsearch:view_log_table_page")
        def view_log_table_page():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/display/INSTASEARCH/instantsearchlogtable")
            page.wait_until_visible((By.ID, "popularTable"))
            page.wait_until_visible((By.ID, "failedTable"))
            page.wait_until_visible((By.ID, "userSearchTable"))
        view_log_table_page()


        @print_timing("selenium_instantsearch:view_macro_page_and_search")
        def view_macro_page_and_search():
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/display/INSTASEARCH/instantsearchmacro")
            page.wait_until_visible((By.CLASS_NAME, "plugin_instantsearch_searchbox"))
            page.get_element((By.CLASS_NAME, "plugin_instantsearch_searchbox")).send_keys("page")
            page.wait_until_visible((By.CLASS_NAME, "plugin_instantsearch_returnedSearchResult"))
        view_macro_page_and_search()

    measure()
