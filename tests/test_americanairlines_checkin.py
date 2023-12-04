from pages.air_american_page import AmericanArilinesCheckinPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class AmericanArilines(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    print(basepath)

    def setUp(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.aa.com/aa/reservation/flightCheckInViewReservationsAccess.do"
        driver.get(desktop_url)

    def test_Americanair_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        driver = self.driver

        #  files Ojects
        Logfile.create_log_file(self)
        AmericanArilinesPageOnj = AmericanArilinesCheckinPage(driver)
        # first name field
        AmericanArilinesPageOnj.first_name()
        # last name
        AmericanArilinesPageOnj.last_nam()
        # confirmation code
        AmericanArilinesPageOnj.confirmation_code()
        # button click
        AmericanArilinesPageOnj.submit_button()
        # Screenshots method
        Screenshots.take_screenshot(self, 'americanairlines')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

