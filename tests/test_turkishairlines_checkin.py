from pages.air_turkish_page import TurkishAirlinesCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Turkishairlines(unittest.TestCase):

    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_Turkishairlines_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://m.turkishairlines.com/#/reservations"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects

        Logfile.create_log_file(self)

        # Create Object and call method of  to fill form
        TurkishAirlinesDesktopPageObj = TurkishAirlinesCheckinDesktopPage(driver)

        # last name
        TurkishAirlinesDesktopPageObj.tab_click()
        TurkishAirlinesDesktopPageObj.confirmation_code()
        TurkishAirlinesDesktopPageObj.last_name()

        # button clicksubmitbtn
        TurkishAirlinesDesktopPageObj.submit_button()

        # Screenshots method
        Screenshots.take_screenshot(self, 'turkishairlines_desktop')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

