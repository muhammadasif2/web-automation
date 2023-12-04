from pages.air_eurowing_page import EurowingCheckinDesktopPage,EurowingCheckinMobilePage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Eurowing(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass

    def test_Eurowing_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py

        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.eurowings.com/skysales/CheckinInfo.aspx?mode=checkin"
        driver.get(desktop_url)
        driver = self.driver
        driver = self.driver
        #  files Ojects
        Logfile.create_log_file(self)

        # Create Object and call method of Aeroligus to fill form
        EurowingDesktopPageObj = EurowingCheckinDesktopPage(driver)

        # first name field

        EurowingDesktopPageObj.confirmation_code()

        # Last name
        EurowingDesktopPageObj.last_name()
        # submit button
        EurowingDesktopPageObj.submit_button()

        # Screenshots method
        Screenshots.take_screenshot(self, 'eurowing_desktop')

    def tearDown(self):
        self.driver.close()

    def test_Eurowing_mobile(self):
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
        desktop_url = "https://mobile.eurowings.com/booking/BookingList.aspx?context=checkin&input=checkin&back=home&culture=en-GB"
        driver.get(desktop_url)

        #  files Ojects
        Logfile.create_log_file(self)

        # Create Object and call method of Aeroligus to fill form
        EurowingMobilePageObj = EurowingCheckinMobilePage(driver)
        # first name field

        EurowingMobilePageObj.first_name()
        # last name
        EurowingMobilePageObj.last_name()

        # button click
        EurowingMobilePageObj.submit_button()
        # wait for error message

        # Screenshots method
        Screenshots.take_screenshot(self, 'eurowing_mobile')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))

