from pages.air_korean_page import KoreanAirCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Koreanair(unittest.TestCase):

    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_Koreanair_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.koreanair.com/global/en.html"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects

        Logfile.create_log_file(self)
        KoreanAirDesktopPageObj = KoreanAirCheckinDesktopPage(driver)
        # first name field
        KoreanAirDesktopPageObj.checkin_tab()
        KoreanAirDesktopPageObj.first_name()

        # last name
        KoreanAirDesktopPageObj.last_name()
        # button clicksubmitbtn
        KoreanAirDesktopPageObj.submit_button()

        # Screenshots method
        Screenshots.take_screenshot(self, 'korean_desktop')

    def tearDown(self):
        self.driver.close()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

