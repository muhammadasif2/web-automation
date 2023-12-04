from pages.air_canada_page import AirCanadaChekinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class Aircanada(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    print(basepath)

    def setUp(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.aircanada.com/us/en/aco/home.html"
        driver.get(desktop_url)

    def test_Aircanada_desktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """

        driver = self.driver
        #  files Ojects
        Logfile.create_log_file(self)

        AirCanadaDesktopPageObj = AirCanadaChekinDesktopPage(driver)
        AirCanadaDesktopPageObj.language_pop_up()
        AirCanadaDesktopPageObj.checkintab_button()

        AirCanadaDesktopPageObj.first_name()

        AirCanadaDesktopPageObj.last_name()

        AirCanadaDesktopPageObj.confirmation_code()

        AirCanadaDesktopPageObj.departure_city()
        # button click
        AirCanadaDesktopPageObj.submit_button()
        # Screenshots method
        Screenshots.take_screenshot(self, 'aircanada')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

