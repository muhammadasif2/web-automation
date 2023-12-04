from pages.air_austrian_page import AustrianAirlinesCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class AustrianAir(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_Austrian_Desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://wci.austrian.com/app/ck.fly"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects
        Logfile.create_log_file(self)
        AustrianAirlinesDesktopPageObj = AustrianAirlinesCheckinDesktopPage(driver)
        # first name field

        AustrianAirlinesDesktopPageObj.last_name()
        # Last name
        AustrianAirlinesDesktopPageObj.confirmation_code()
        # submit button
        AustrianAirlinesDesktopPageObj.submit_button()
        # Screenshots method
        Screenshots.take_screenshot(self, 'austrian__desktop')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

