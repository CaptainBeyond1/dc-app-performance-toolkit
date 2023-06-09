import dateutil.parser
import datetime
import pytz
from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:verify_that_reminder_has_been_sent")
        def sub_measure():
            # open page by id in edit mode
            page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/display/TEST/test+page")

            # wait for page reminder icon/ link to be ready
            page.wait_until_visible((By.ID, "page-reminders-action"))

            # activate status window
            page.get_element((By.XPATH,".//*[@id='page-reminders-action']")).click()

            # wait for list of reminders
            page.wait_until_visible((By.ID, "page-reminders-list-new"))

            # get last sent datetime from table cell (assuming there is just one reminder and ours is the first)
            last_sent_cell \
                = page.get_element((By.XPATH,"/html/body/section[1]/div/div[2]/div/table/tbody/tr/td[3]"))
            last_sent_datetime = dateutil.parser.parse(last_sent_cell.text)

            current_datetime = datetime.datetime.now(pytz.utc)
            last_sent_datetime = last_sent_datetime.astimezone(pytz.utc)
            threshold_datetime = current_datetime - datetime.timedelta(seconds=120)

            print("threshold_datetime:", threshold_datetime)
            print("last_sent_datetime:", last_sent_datetime)
            print("current_datetime:", current_datetime)


            # only if it's not older than 120 seconds the test succeeds
            assert last_sent_datetime > threshold_datetime

        sub_measure()
    measure()
