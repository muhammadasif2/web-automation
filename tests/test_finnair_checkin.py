from pages.air_finn_page import FinnAirCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Finnair(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    print(basepath)

    def setUp(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://checkin.si.amadeus.net/static/PRD/AY/#/identification"
        driver.get(desktop_url)

    def test_Finnair_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        driver = self.driver
        #  files Ojects
        Logfile.create_log_file(self)
        FinnAirDesktopPageObj = FinnAirCheckinDesktopPage(driver)
        # url fragment test
        FinnAirDesktopPageObj.url_fragment()

        # confirmation_code
        FinnAirDesktopPageObj.confirmation_code()
        # last_name
        FinnAirDesktopPageObj.last_name()

        FinnAirDesktopPageObj.submit_button()
        # Screenshots method
        Screenshots.take_screenshot(self, 'finnair')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

