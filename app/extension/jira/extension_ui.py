import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    actions = ActionChains(webdriver)

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:create_chart")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/dependencymapper")
            time.sleep(2)
            driver.save_screenshot("awaitforinputvisible.png")
            page.wait_until_visible((By.ID, "jqlInput"))
            time.sleep(1)
            driver.save_screenshot("awaitforinput.png")
            jql = page.get_element((By.ID, "jqlInput"))
            time.sleep(1)
            jql.clear()
            jql.send_keys('project=TEST')
            jql.send_keys(Keys.ENTER)
            driver.save_screenshot("awaitfordepSummary.png")
            page.wait_until_visible((By.ID, "depSummary"))
        sub_measure()

        @print_timing("selenium_app_custom_action:refresh_chart")
        def sub_measure():
            actions.send_keys(Keys.ENTER)
            actions.perform()
            page.wait_until_visible((By.ID, "depSummary"))
        sub_measure()

        @print_timing("selenium_app_custom_action:view_charts")
        def sub_measure():
            page.wait_until_visible((By.ID, "buttonDepRing"))
            page.get_element((By.ID, "buttonDepRing")).click()
            page.wait_until_visible((By.ID, "ringChart"))
            page.get_element((By.ID, "buttonDepTimeline")).click()
            page.wait_until_visible((By.ID, "timelineChart"))
            page.get_element((By.ID, "buttonDepSankey")).click()
            page.wait_until_visible((By.ID, "sankeyChart"))
            page.get_element((By.ID, "buttonDepHeatmap")).click()
            page.wait_until_visible((By.ID, "tableChart"))
            page.get_element((By.ID, "buttonDepForce")).click()
            page.wait_until_visible((By.ID, "forceChart"))
            page.get_element((By.ID, "buttonDepSpider")).click()
            page.wait_until_visible((By.ID, "spiderChart"))
            page.get_element((By.ID, "buttonDepTimeToResolve")).click()
            page.wait_until_visible((By.ID, "timeToResolveChart"))
        sub_measure()
    measure()
