import string
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium.webdriver.common.keys import Keys
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    letters = string.ascii_lowercase
    testfieldValue = ''.join(random.choice(letters) for i in range(10))

    @print_timing("selenium_app_specific_user_login")
    def measure():
        def app_specific_user_login(username='admin', password='admin'):
            login_page = Login(webdriver)
            login_page.delete_all_cookies()
            login_page.go_to()
            login_page.set_credentials(username=username, password=password)
            if login_page.is_first_login():
                login_page.first_login_setup()
            if login_page.is_first_login_second_page():
                login_page.first_login_second_page_setup()
            login_page.wait_for_page_loaded()
        app_specific_user_login(username='admin', password='admin')
    measure()

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:create_request")
        def sub_measure():
            actions = ActionChains(webdriver)
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/CallViewAction.jspa?reporter=admin&testfield={testfieldValue}")
            page.wait_until_visible((By.ID, "create_link"))
            page.get_element((By.ID, "create_link")).click()
            page.wait_until_visible((By.ID, "summary"))
            page.get_element((By.ID, "summary")).click()
            actions.send_keys(''.join(random.choice(letters) for i in range(10))).perform();
            page.get_element((By.ID, "reporter-field")).click()
            page.get_element((By.ID, "create-issue-submit")).click()
            time.sleep(6)
        sub_measure()
    measure()

