
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from  testvalues import Testvalues


class AerolingusCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "aerolingus"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def first_name(self):

        # for First Name test
        try:

            element = self.driver.find_element(By.ID, "pnr-1")

            if element:
                logging.info(self.site_name + " :Booking Reference field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: Booking Reference element is not attached to the page document")
            self.driver.find_element(By.ID, "pnr-1").clear()

            self.driver.find_element(By.ID, "pnr-1").send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: Booking Reference element is not attached to the page document")

    def last_name(self):
        # for last name test
        try:

            element = self.driver.find_element(By.ID, "surname-2")

            if element:
                logging.info(self.site_name + " :Last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: Last name element is not attached to the page document")
            self.driver.find_element(By.ID, "surname-2").clear()

            self.driver.find_element(By.ID, "surname-2").send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: Last name element is not attached to the page document")

    def submit_button(self):
        # submitting form

        element = self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click^="submitCheckin"]')
        if element:
            element.click()
            logging.info(self.site_name + " :submit button exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

    #  for error Message
        element = WebDriverWait(
            self.driver,
            30

        ).until(EC.presence_of_element_located((By.CSS_SELECTOR,'form[name="form.flightCheckin"] div[ng-attr-class*="error"] div[id="message-text-1"]')))

        if element:
            logging.info(self.site_name + " :error message exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")