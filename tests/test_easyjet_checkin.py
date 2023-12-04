from pages.air_easyjet_page import EasyjetCheckinMobilePage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Easyjet(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        mobile_emulation = {"deviceName": "iPhone 6/7/8"}

        # Define a variable to hold all the configurations we want
        chrome_options = webdriver.ChromeOptions()
        # Add the mobile emulation to the chrome options variable
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # Create driver, pass it the path to the chromedriver file and the special configurations you want to run
        self.driver = webdriver.Chrome(
            options=chrome_options)
        # self.driver = webdriver.Chrome()

    def test_Delta_mobile(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        driver = self.driver
        desktop_url = "https://www.easyjet.com/en/?chkin=1"
        driver.get(desktop_url)

        #  files Ojects
        Logfile.create_log_file(self)
        EasyjetMobilePageObj = EasyjetCheckinMobilePage(driver)
        # first name field
        EasyjetMobilePageObj.Passenger_radio_button()
        # confirmation code box
        EasyjetMobilePageObj.confirmation_code()
        # last name
        EasyjetMobilePageObj.last_name()

        # button click
        EasyjetMobilePageObj.submit_button()

        Screenshots.take_screenshot(self, 'easyjet_mobile')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

