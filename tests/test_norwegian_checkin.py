from pages.air_norwegian_page import NorwegianCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Norwegian(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    print(basepath)

    def setUp(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.norwegian.com/us/ipr/CheckIn#/auth/lookup"
        driver.get(desktop_url)

    def test_Norwegian_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        driver = self.driver
        #  files Ojects
        Logfile.create_log_file(self)
        NorwegianDesktopPageObj = NorwegianCheckinDesktopPage(driver)
        # confirmation_code
        NorwegianDesktopPageObj.confirmation_code()
        # last name
        NorwegianDesktopPageObj.last_name()

        # button click
        NorwegianDesktopPageObj.submit_button()
        # Screenshots method
        Screenshots.take_screenshot(self, 'norwegian')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

