from pages.air_qatar_page import QatarAirCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath
import  logging
import  datetime

class Qatarair(unittest.TestCase):

    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_Qatarair_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://cki.qatarairways.com/cki-web/pages/search.xhtml"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects

        Logfile.create_log_file(self)

        QatarAirDesktopPageObj = QatarAirCheckinDesktopPage(driver)

        # last name
        QatarAirDesktopPageObj.last_name()
        QatarAirDesktopPageObj.confirmation_code()

        # button clicksubmitbtn
        QatarAirDesktopPageObj.submit_button()

        # Screenshots method
        Screenshots.take_screenshot(self, 'qatarair_desktop')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

