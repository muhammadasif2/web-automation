from pages.air_japan_page import JapanAirlinesCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Japanairlines(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    print(basepath)

    def setUp(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://checkin.si.amadeus.net/static/PRD/JL/#/checkin?ghAirline=JL&ln=en"
        driver.get(desktop_url)

    def test_Japanairlines_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        driver = self.driver

        #  files Ojects
        Logfile.create_log_file(self)
        JapanAirlinesDesktopPageObj = JapanAirlinesCheckinDesktopPage(driver)
        JapanAirlinesDesktopPageObj.click_tab()
        # confimation filed
        JapanAirlinesDesktopPageObj.confirmation_code()
        # last name
        JapanAirlinesDesktopPageObj.last_name()
        JapanAirlinesDesktopPageObj.first_name()
        # flight number
        JapanAirlinesDesktopPageObj.fligh_number()
        # button click
        JapanAirlinesDesktopPageObj.submit_button()
        # Screenshots method
        Screenshots.take_screenshot(self, 'japanairlines')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

