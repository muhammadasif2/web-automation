from pages.air_china_southern_page import ChinaSouthernCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Chinasouthern(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    print(basepath)

    def setUp(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "http://airport.csair.com/webcki/login/login.air"
        driver.get(desktop_url)

    def test_Chinasouthern_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        driver = self.driver

        #  files Ojects
        Logfile.create_log_file(self)

        # Create Object and call method of Aeroligus to fill form
        ChinaSouthernDesktopPageObj = ChinaSouthernCheckinDesktopPage(driver)
        # first name field
        ChinaSouthernDesktopPageObj.ticket_number()
        # last name
        ChinaSouthernDesktopPageObj.last_name()
        # button click
        ChinaSouthernDesktopPageObj.submit_button()
        # Screenshots method
        Screenshots.take_screenshot(self, 'chinasouthern')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

