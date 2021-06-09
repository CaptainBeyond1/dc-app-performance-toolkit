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
        @print_timing("selenium_app_custom_action")
        def sub_measure():
            actions = ActionChains(webdriver)
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/CurrencyHistoryItemsViewAction.jspa")
            page.wait_until_visible((By.CLASS_NAME, "add-row"))
            page.get_element((By.CLASS_NAME, "add-row")).click()
            page.wait_until_visible((By.ID, "s2id_organization-select"))
            page.get_element((By.ID, "s2id_organization-select")).click()
            actions.send_keys(Keys.ARROW_DOWN).perform()
            actions.send_keys(Keys.ENTER).perform();
            page.get_element((By.ID, "s2id_country-select")).click()
            actions.send_keys(Keys.ARROW_DOWN).perform()
            actions.send_keys(Keys.ENTER).perform();
            page.get_element((By.ID, "s2id_fromCurrency-select")).click()
            actions.send_keys(Keys.ARROW_DOWN).perform()
            actions.send_keys(Keys.ENTER).perform();
            page.get_element((By.ID, "s2id_toCurrency-select")).click()
            actions.send_keys(Keys.ARROW_DOWN).perform()
            actions.send_keys(Keys.ARROW_DOWN).perform()
            actions.send_keys(Keys.ENTER).perform();
            page.get_element((By.ID, "currencyInput")).click()
            actions.send_keys('1').perform();
            page.get_element((By.ID, "submit-creation")).click()
            page.findElement(By.XPATH("//a[@href='AutomatedImportsViewAction.jspa']")).click()
            page.wait_until_visible((By.ID, "button-automated-import"))
            page.get_element((By.ID, "button-automated-import")).click()
        sub_measure()
    measure()

