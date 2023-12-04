from pages.air_aeroflot_page import  AeroflotCheckinDesktopPage
import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile

from os.path import dirname, realpath
import time


class Aeroflot(unittest.TestCase):
    """A sample test class to show how page object works"""

    filepath = realpath(__file__)
    basepath = dirname(filepath)
    # print(basepath)

    def setUp(self):
        pass
        # self.driver = webdriver.Chrome()

    def test_AeroflotDesktop(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.walmart.com/ip/BODYARMOR-Sports-Drink-Tropical-Punch-12-fl-oz-8-count/441450820?athcpid=441450820&athpgid=AthenaHomepageDesktop__mixed__0.77&athcgid=null&athznid=SeasonalCampaigns_d32ce95c-381f-4c57-b60b-031c5eef8950_items&athieid=null&athstid=CS020&athguid=Cb0jDbzOy6Bj_FF45SwaUstKajsz_3Og9U2u&athancid=null&athena=true"
        driver.get(desktop_url)
        driver = self.driver
        #  files Ojects
        Logfile.create_log_file(self)

        AeroflotCheckinDesktopPagObj = AeroflotCheckinDesktopPage(driver)
        time.sleep(.5)
        AeroflotCheckinDesktopPagObj.first_name()

        AeroflotCheckinDesktopPagObj.last_name()

        AeroflotCheckinDesktopPagObj.submit_button()

        Screenshots.take_screenshot(self, 'aeroflot_desktop')

    def tearDown(self):
        self.driver.close()
        self.driver.stop()

   

# if __name__ == "__main__":
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/webautomation/reports'))

