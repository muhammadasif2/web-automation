from pages.air_lotpolish_page import LotPolishCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Lotpolish(unittest.TestCase):

    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_Lotpolish_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://checkin.si.amadeus.net/static/PRD/LO/#/identification"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects

        Logfile.create_log_file(self)

        LotPolishDesktopPageObj = LotPolishCheckinDesktopPage(driver)
        # first name field

        LotPolishDesktopPageObj.tab_click()

        # last name
        LotPolishDesktopPageObj.last_name()
        LotPolishDesktopPageObj.confirmation_code()

        # button clicksubmitbtn
        LotPolishDesktopPageObj.submit_button()

        # Screenshots method
        Screenshots.take_screenshot(self, 'lotpolish_desktop')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

