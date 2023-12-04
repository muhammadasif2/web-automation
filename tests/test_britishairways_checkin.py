from pages.air_british_page import BritishAirCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class British(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    print(basepath)

    def setUp(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.britishairways.com/travel/olcilandingpageauthreq/public/en_us?link=main_nav"
        driver.get(desktop_url)

    def test_BritishDesktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        driver = self.driver

        #  files Ojects
        Logfile.create_log_file(self)
        BritishAirDesktopPageObj = BritishAirCheckinDesktopPage(driver)
        # first name field
        BritishAirDesktopPageObj.confirmation_code()
        # last name
        BritishAirDesktopPageObj.last_name()
        # button click
        BritishAirDesktopPageObj.submit_button()
        # Screenshots method
        Screenshots.take_screenshot(self, 'britishairlines')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

