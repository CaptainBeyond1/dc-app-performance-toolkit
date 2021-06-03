import string
import random

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

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:create_issue_from_link")
        def sub_measure():
            actions = ActionChains(webdriver)
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/CallViewAction.jspa?reporter={datasets['username']}")
            page.wait_until_visible((By.ID, "create_link"))
            page.get_element((By.ID, "create_link")).click()
            page.wait_until_visible((By.ID, "summary"))
            page.get_element((By.ID, "summary")).click()
            actions.send_keys(''.join(random.choice(letters) for i in range(10))).perform();
            page.get_element((By.ID, "create-issue-submit")).click()
        sub_measure()
    measure()

