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
    letters = string.ascii_lowercase

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
        @print_timing("selenium_app_custom_action:create_poll")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/hr360survey.jspa?page=survey")
            page.wait_until_visible((By.ID, "survey-name"))
            name = page.get_element((By.ID, "survey-name"))
            name.send_keys(''.join(random.choice(letters) for i in range(10)));
            webdriver.save_screenshot('1.png')
            page.wait_until_visible((By.ID, "survey-due-date"))
            date = page.get_element((By.ID, "survey-due-date"))
            date.send_keys('2021-11-28')
            webdriver.save_screenshot('2.png')
            page.wait_until_visible((By.NAME, "category"))
            page.get_element((By.NAME, "category")).click()
            webdriver.save_screenshot('3.png')
            page.get_element((By.ID, "aui-uid-1")).click()
            respondent = page.get_element((By.ID, "selected-respondent"))
            respondent.send_keys('admin')
            webdriver.save_screenshot('4.png')
            page.get_element((By.ID, "add-respondent-button")).click()
            whom = page.get_element((By.ID, "selected-whom"))
            whom.send_keys('admin')
            page.get_element((By.ID, "add-whom-button")).click()
            webdriver.save_screenshot('5.png')
            save_buttons = page.get_elements((By.CLASS_NAME, "save-newsurvey"))
            save_buttons[1].click()
            webdriver.save_screenshot('final.png')
        sub_measure()

        @print_timing("selenium_app_custom_action:evaluate_poll")
        def sub_measure():
            webdriver.implicitly_wait(1)
            webdriver.save_screenshot('00(2).png')
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/hr360account.jspa")
            webdriver.save_screenshot('0(2).png')
            page.wait_until_visible((By.CLASS_NAME, "hr360-survey-inner-container"))
            surveys = page.get_elements((By.CLASS_NAME, "hr360-survey-inner-container"))
            surveys[0].click()
            users = page.get_elements((By.NAME, "admin"))
            users[0].click()
            answers = page.get_elements((By.NAME, "1"))
            answers[0].click()
            webdriver.save_screenshot('1(2).png')
            webdriver.save_screenshot('2(2).png')
            page.get_element((By.ID, "hr360-comp-dialog-submit-button")).click()
            webdriver.save_screenshot('final2.png')
        sub_measure()
    measure()

