from pages.air_allnippon_page import AllnipponCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Allnipponair(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    print(basepath)

    def setUp(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://aswbe-i.ana.co.jp/international_asw/pages/webcheckin/checkin_search_input.xhtml?CONNECTION_KIND=JPN&LANG=en"
        driver.get(desktop_url)

    def test_Allnippon_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        driver = self.driver

        #  files Ojects
        Logfile.create_log_file(self)

        AllnipponDesktopPageObj = AllnipponCheckinDesktopPage(driver)
        # confirmation code
        AllnipponDesktopPageObj.confirmation_code()
        # first name field
        AllnipponDesktopPageObj.first_name()
        # last name
        AllnipponDesktopPageObj.last_name()
        # button click
        AllnipponDesktopPageObj.submit_button()
        # Screenshots method
        Screenshots.take_screenshot(self, 'allnipponair')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

