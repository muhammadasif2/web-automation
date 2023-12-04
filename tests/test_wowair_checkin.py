from pages.air_wow_page import WowAirCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Wowair(unittest.TestCase):

    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_Wowair_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://wowair.us/web-check-in/"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects

        Logfile.create_log_file(self)

        # Create Object and call method of  to fill form
        WowAirDesktopPageObj = WowAirCheckinDesktopPage(driver)
        # first name field

        WowAirDesktopPageObj.confirmation_code()

        # last name
        WowAirDesktopPageObj.last_name()
        # button clicksubmitbtn
        WowAirDesktopPageObj.submit_button()

        # Screenshots method
        Screenshots.take_screenshot(self, 'wowair_desktop')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

