import random
import string

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium_ui.jsm.pages.customer_pages import Login
from util.conf import JSM_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    letters = string.ascii_lowercase

    @print_timing("selenium_customer_app_custom_action")
    def measure():

        @print_timing("selenium_customer_app_custom_action:create_another_request")
        def sub_measure():
            action = ActionChains(webdriver)
            page.go_to_url(f"{JSM_SETTINGS.server_url}/servicedesk/customer/portal/86/create/882")
            page.wait_until_visible((By.ID, "summary"))
            name = page.get_element((By.ID, "summary"))
            name.send_keys(''.join(random.choice(letters) for i in range(10)));
            page.wait_until_visible((By.ID, "customfield_10600"))
            testfield = page.get_element((By.ID, "customfield_10600"))
            testfield.click()
            testfield.send_keys(''.join(random.choice(letters) for i in range(10)))
            page.wait_until_visible((By.ID, "create-another-button"))
            createanother = page.get_element((By.ID, "create-another-button"))
            createanother.click()
            page.wait_until_visible((By.ID, 'create-another-button'))
            action.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.CONTROL).key_up(Keys.TAB).perform();
            action.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.CONTROL).key_up(Keys.TAB).perform();
            action.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.CONTROL).key_up(Keys.TAB).perform();
        sub_measure()
    measure()
