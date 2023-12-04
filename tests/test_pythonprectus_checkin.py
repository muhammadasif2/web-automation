import unittest
from selenium import webdriver
from screenshotscode import Screenshots
from logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class SelectTests():

    def desktoptest(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        desktop_url = "https://www.eurowings.com/skysales/CheckinInfo.aspx?mode=checkin"
        driver.get(desktop_url)
        driver = self.driver

    def mobiletest(self):

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