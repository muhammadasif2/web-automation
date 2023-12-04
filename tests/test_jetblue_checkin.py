from pages.air_jetblue_page import JetblueCheckinDesktopPage,JetbluecheckinMobilePaage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath
import time


class Jetblue(unittest.TestCase):

    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_Jetblue_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://checkin.jetblue.com/"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects
        time.sleep(.5)
        Logfile.create_log_file(self)
        JetblueDesktopPageObj = JetblueCheckinDesktopPage(driver)
        # first name field
        JetblueDesktopPageObj.first_name()

        # last name
        JetblueDesktopPageObj.last_name()
        JetblueDesktopPageObj.airport_code()
        JetblueDesktopPageObj.confirmation_code()
        # button clicksubmitbtn
        JetblueDesktopPageObj.submit_button()

        # Screenshots method
        Screenshots.take_screenshot(self, 'jetblue_desktop')

    def tearDown(self):
        self.driver.close()

    def test_Jetblue_mobile(self):
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
        desktop_url = "https://mobilecheckin.jetblue.com/checkin/check-in"
        driver.get(desktop_url)

        #  files Ojects
        Logfile.create_log_file(self)
        JetblueMobilePaageObj = JetbluecheckinMobilePaage(driver)
        # first name field

        JetblueMobilePaageObj.first_name()

        # last name
        JetblueMobilePaageObj.last_name()

        JetblueMobilePaageObj.confirmation_code()

        JetblueMobilePaageObj.airport_code()

        # button click
        JetblueMobilePaageObj.submit_button()
        # wait for error message

        # Screenshots method
        Screenshots.take_screenshot(self, 'jetblue_mobile')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

