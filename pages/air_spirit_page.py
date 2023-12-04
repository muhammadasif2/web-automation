from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class SpiritAirCheckinDesktop():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "spiritairlines"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def tab_click(self):
        try:
            element = self.driver.find_element_by_link_text('Check-In')

            if element:
                element.click()
                logging.info(self.site_name + " :clicking check-in tab to make it active")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")

    def confirmation_code(self):
        # for last name test
        # for confirmation code test
        try:

            element = self.driver.find_element(By.NAME, "recordLocator")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.NAME, "recordLocator").clear()

            self.driver.find_element(By.NAME, "recordLocator").send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def last_name(self):
        # for last name test
        try:

            element = self.driver.find_element(By.NAME, 'lastName')

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.NAME, 'lastName').clear()

            self.driver.find_element(By.NAME, 'lastName').send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):

        # submitting form
        # try:
        element = WebDriverWait(
            self.driver,
            100

        ).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'form button')))

        if element:
            element.click()
            logging.info(self.site_name + " :submit button exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")
