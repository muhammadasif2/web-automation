from pages.air_emirates_page import EmiratesCheckinDesktopPage,EmiratesCheckinMobilePage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Emirates(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_Emirates_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.emirates.com/us/english/plan_book/check_in_online/online-check-in.aspx"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects
        Logfile.create_log_file(self)
        EmiratesDesktopPageObj = EmiratesCheckinDesktopPage(driver)
        EmiratesDesktopPageObj.checkin_tab()
        # first name field

        EmiratesDesktopPageObj.confirmation_code()

        # Last name
        EmiratesDesktopPageObj.last_name()
        # submit button
        EmiratesDesktopPageObj.submit_button()
        # wait for error message

        # Screenshots method
        Screenshots.take_screenshot(self, 'emirates')

    def tearDown(self):
        self.driver.close()

    def test_Emirates_mobile(self):
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
        desktop_url = "https://mobile.emirates.com/us/english/CKIN/OLCI/flightInfo.xhtml"
        driver.get(desktop_url)

        #  files Ojects
        Logfile.create_log_file(self)
        EmiratesMobilePageObj = EmiratesCheckinMobilePage(driver)
        # first name field

        EmiratesMobilePageObj.confirmation_code()
        # last name
        EmiratesMobilePageObj.last_name()

        # button click
        EmiratesMobilePageObj.submit_button()

        Screenshots.take_screenshot(self, 'emirates_mobile')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

