from pages.air_sas_page import SasCheckinDesktopPage, SasCheckinMobilePage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Sas(unittest.TestCase):

    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_sas_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.flysas.com/en/us/Generic/Services/Checkin/"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects

        Logfile.create_log_file(self)

        SasDesktopPageObj = SasCheckinDesktopPage(driver)
        # first name field

        SasDesktopPageObj.click_tab()

        SasDesktopPageObj.confirmation_code()

        # last name
        SasDesktopPageObj.email_test()
        # button clicksubmitbtn
        SasDesktopPageObj.submit_button()
        # wait for error message

        # Screenshots method
        Screenshots.take_screenshot(self, 'sas_desktop')

    def tearDown(self):
        self.driver.close()

    def test_Sas_mobile(self):
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
        desktop_url = "https://ci.sas.mobi/ci/default.aspx"
        driver.get(desktop_url)

        #  files Ojects
        Logfile.create_log_file(self)
        SasMobilePageObj = SasCheckinMobilePage(driver)
        SasMobilePageObj.last_name()
        SasMobilePageObj.confirmation_code()

        SasMobilePageObj.submit_button()

        Screenshots.take_screenshot(self, 'sas')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

