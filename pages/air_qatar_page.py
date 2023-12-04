from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class QatarAirCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "qatarair"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def last_name(self):

        # for last name test
        try:
            element = WebDriverWait(
                self.driver,
                20

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="lastname"]')))

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, "input[name=\"lastname\"]").clear()
            self.driver.find_element(By.CSS_SELECTOR, "input[name=\"lastname\"]").send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def confirmation_code(self):
        # for confirmation code test
        try:

            element = self.driver.find_element(By.NAME, "pnr")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.NAME, "pnr").clear()
            self.driver.find_element(By.NAME, "pnr").send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def submit_button(self):

        # submitting form

        element = self.driver.find_element_by_link_text('Check in')
        if element:
            element.click()
            logging.info(self.site_name + " :submit button exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        # except Exception:
        #     logging.error(
        #         self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        try:
            element = WebDriverWait(
                self.driver,
                10

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id="service-msg"] p')))

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.error(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")
