import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:create_chart")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/dependencymapper")
            webdriver.save_screenshot('1.png')
            page.wait_until_visible((By.ID, "jqlInput"))
            jql = page.get_element((By.ID, "jqlInput"))
            jql.clear()
            webdriver.save_screenshot('clear.png')
            jql.send_keys('project=TEST')
            webdriver.save_screenshot('2.png')
            page.wait_until_visible((By.ID, "firstVizButton"))
            page.get_element((By.ID, "firstVizButton")).click()
            webdriver.save_screenshot('boardChart.png')
            page.wait_until_visible((By.ID, "boardChart"))
            webdriver.save_screenshot('3.png')
        sub_measure()

        @print_timing("selenium_app_custom_action:refresh_chart")
        def sub_measure():
            page.wait_until_visible((By.ID, "firstVizButton"))
            page.get_element((By.ID, "firstVizButton")).click()
            webdriver.save_screenshot('refresh.png')
            page.wait_until_visible((By.ID, "boardChart"))
            webdriver.save_screenshot('refresh.png')
        sub_measure()

        @print_timing("selenium_app_custom_action:create_additional_charts")
        def sub_measure():
            page.get_element((By.ID, "buttonDepRing")).click()
            page.wait_until_visible((By.ID, "ringChart"))
            webdriver.save_screenshot('4.png')
            page.get_element((By.ID, "buttonDepTimeline")).click()
            page.wait_until_visible((By.ID, "timelineChart"))
            webdriver.save_screenshot('timelineChart.png')
            page.get_element((By.ID, "buttonDepSankey")).click()
            page.wait_until_visible((By.ID, "sankeyChart"))
            webdriver.save_screenshot('5.png')
            page.get_element((By.ID, "buttonDepHeatmap")).click()
            page.wait_until_visible((By.ID, "tableChart"))
            webdriver.save_screenshot('6.png')
            page.get_element((By.ID, "buttonDepForce")).click()
            page.wait_until_visible((By.ID, "forceChart"))
            webdriver.save_screenshot('7.png')
            page.get_element((By.ID, "buttonDepSpider")).click()
            page.wait_until_visible((By.ID, "spiderChart"))
            webdriver.save_screenshot('8.png')
            page.get_element((By.ID, "buttonDepTimeToResolve")).click()
            page.wait_until_visible((By.ID, "timeToResolveChart"))
            webdriver.save_screenshot('9.png')
        sub_measure()
    measure()

