from pages.air_catheypacific_page import CatheyPacificChekinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Catheypacific(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    print(basepath)

    def setUp(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.cathaypacific.com/olci/#/en_US/login"
        driver.get(desktop_url)

    def test_Catheypacific_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        driver = self.driver

        #  files Ojects
        Logfile.create_log_file(self)
        CatheyPacificDesktopPageObj = CatheyPacificChekinDesktopPage(driver)
        # first name field
        CatheyPacificDesktopPageObj.first_name()
        # last name
        CatheyPacificDesktopPageObj.last_name()
        # confirmation code
        CatheyPacificDesktopPageObj.confirmation_code()
        # button click
        CatheyPacificDesktopPageObj.submit_button()
        # Screenshots method
        Screenshots.take_screenshot(self, 'catheypacific_desktop')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

