from pages.air_aeromexico_page import AeromexicoCheckinDesktopPagae
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Aeromexico(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    print(basepath)

    def setUp(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://aeromexico.com/en-us/check-in"
        driver.get(desktop_url)

    def test_Aeromexico_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        driver = self.driver
        #  files Ojects
        Logfile.create_log_file(self)

        AeromexicoDesktopPagaeObj = AeromexicoCheckinDesktopPagae(driver)

        AeromexicoDesktopPagaeObj.confirmation_code()

        AeromexicoDesktopPagaeObj.last_name()

        AeromexicoDesktopPagaeObj.submit_button()
        # Screenshots method
        Screenshots.take_screenshot(self, 'aeromexico')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

