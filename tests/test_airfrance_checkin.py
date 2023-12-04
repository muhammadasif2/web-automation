from pages.air_france_page import AirFranceCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath
from testvalues import Testvalues
import time
import nose.tools


class Airfrance(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_AirfranceDesktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "http://www.airfrance.us/US/en/local/core/engine/echeckin/IciFormAction.do"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects
        Logfile.create_log_file(self)

        AirFranceDesktopPageObj = AirFranceCheckinDesktopPage(driver)
        # pop up
        AirFranceDesktopPageObj.popup_button()

        AirFranceDesktopPageObj.confirmation_code()

        # first name field
        AirFranceDesktopPageObj.flight_carrer_code()

        # flight carrer code
        AirFranceDesktopPageObj.flight_number()
        # submit button
        AirFranceDesktopPageObj.submit_button()

        # Screenshots method
        Screenshots.take_screenshot(self, 'airfrance_desktop')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

