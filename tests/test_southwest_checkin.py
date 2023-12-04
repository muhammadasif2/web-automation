from pages.air_southwest_page import SouthWestCheckinDesktopPage,SouthWestCheckinMobilePage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Southwest(unittest.TestCase):

    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_Southwest_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.southwest.com/flight/retrieveCheckinDoc.html"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects

        Logfile.create_log_file(self)

        SouthWestDesktopPageObj = SouthWestCheckinDesktopPage(driver)
        # first name field

        SouthWestDesktopPageObj.confirmation_code()

        # first name
        SouthWestDesktopPageObj.first_name()
        # last name
        SouthWestDesktopPageObj.last_name()
        # button clicksubmitbtn
        SouthWestDesktopPageObj.submit_button()
        # wait for error message

        # Screenshots method
        Screenshots.take_screenshot(self, 'southwest_desktop')

    def tearDown(self):
        self.driver.close()

    def test_Southwest_mobile(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        mobile_emulation = {"deviceName": "iPhone 6/7/8"}

        # Define a variable to hold all the configurations we want
        chrome_options = webdriver.ChromeOptions()
        # Add the mobile emulation to the chrome options variable
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # Create driver, pass it the path to the chromedriver file and the special configurations you want to run
        self.driver = webdriver.Chrome(
            options=chrome_options)

        driver = self.driver
        desktop_url = "https://mobile.southwest.com/check-in"
        driver.get(desktop_url)

        #  files Ojects
        Logfile.create_log_file(self)

        SouthWestMobilePageObj = SouthWestCheckinMobilePage(driver)

        SouthWestMobilePageObj.confirmation_code()

        # first name
        SouthWestMobilePageObj.first_name()
        # last name
        SouthWestMobilePageObj.last_name()
        # button clicksubmitbtn
        SouthWestMobilePageObj.submit_button()
        # wait for error message
        # Screenshots method
        Screenshots.take_screenshot(self, 'southwest_mobile')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

