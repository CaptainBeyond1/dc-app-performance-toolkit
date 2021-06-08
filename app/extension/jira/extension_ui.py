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

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:view_issue")
        def sub_measure():
            actions = ActionChains(webdriver)
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/CurrencyHistoryItemsViewAction.jspa")
            webdriver.save_screenshot('beforewait.png')
            page.wait_until_visible((By.CLASS_NAME, "add-row"))
            webdriver.save_screenshot('screenie.png')
            page.get_element((By.CLASS_NAME, "add-row")).click()
            page.wait_until_visible((By.ID, "s2id_organization-select"))
            page.get_element((By.ID, "s2id_organization-select")).click()
            actions.send_keys(Keys.ARROW_DOWN).perform()
            actions.send_keys(Keys.ENTER).perform();
            webdriver.save_screenshot('screenie1.png')
            page.get_element((By.ID, "s2id_country-select")).click()
            actions.send_keys(Keys.ARROW_DOWN).perform()
            actions.send_keys(Keys.ENTER).perform();
            page.get_element((By.ID, "s2id_fromCurrency-select")).click()
            actions.send_keys(Keys.ARROW_DOWN).perform()
            actions.send_keys(Keys.ENTER).perform();
            page.get_element((By.ID, "s2id_toCurrency-select")).click()
            webdriver.save_screenshot('screenie2.png')
            actions.send_keys(Keys.ARROW_DOWN).perform()
            actions.send_keys(Keys.ARROW_DOWN).perform()
            actions.send_keys(Keys.ENTER).perform();
            page.get_element((By.ID, "currencyInput")).click()
            actions.send_keys('1').perform();
            webdriver.save_screenshot('screenie2.png')
            page.get_element((By.ID, "submit-creation")).click()
            webdriver.save_screenshot('screenieFinal.png')
        sub_measure()
    measure()

