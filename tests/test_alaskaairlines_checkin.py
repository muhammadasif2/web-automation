from pages.air_alaska_page import AlaskaAirCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath
from testvalues import Testvalues
import time


class Alaskaair(unittest.TestCase):

    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_AlaskaairDesktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://webselfservice.alaskaair.com/checkinweb/Default.aspx"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects
        time.sleep(.5)
        Logfile.create_log_file(self)

        AlaskaAirDesktopPageObj = AlaskaAirCheckinDesktopPage(driver)

        # first name field
        AlaskaAirDesktopPageObj.checkin_city()

        # last name
        AlaskaAirDesktopPageObj.last_name()
        # submit button
        AlaskaAirDesktopPageObj.submit_button()
        # wait for error message

        Screenshots.take_screenshot(self, 'alaska_desktop')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

