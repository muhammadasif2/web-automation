from pages.air_brussel_page import BrusselAirlinesCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath
from testvalues import Testvalues


class Brusselairlines(unittest.TestCase):
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

    def test_Brusselairlines_mobile(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        driver = self.driver
        desktop_url = "https://m.checkin.brusselsairlines.com/mb/MobileForms/PaxByQuery.aspx"
        driver.get(desktop_url)

        #  files Ojects
        Logfile.create_log_file(self)

        BrusselAirlinesDesktopPageObj = BrusselAirlinesCheckinDesktopPage(driver)
        # first name field

        BrusselAirlinesDesktopPageObj.confirmation_code()

        # last name
        BrusselAirlinesDesktopPageObj.last_name()

        # button click
        BrusselAirlinesDesktopPageObj.submit_button()

        Screenshots.take_screenshot(self, 'brusselairlines_mobile')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

