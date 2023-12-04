from pages.air_klm_page import KlmCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Klm(unittest.TestCase):

    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_Klm_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.klm.com/ams/checkin/web/kl/us/en"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects

        Logfile.create_log_file(self)
        KlmDesktopPageObj = KlmCheckinDesktopPage(driver)
        # first name field

        KlmDesktopPageObj.cookied_popup()

        # last name
        KlmDesktopPageObj.flight_carrier_code()
        KlmDesktopPageObj.flight_number()

        # button clicksubmitbtn
        KlmDesktopPageObj.submit_button()

        # Screenshots method
        Screenshots.take_screenshot(self, 'klm_desktop')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

