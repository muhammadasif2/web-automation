from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class KlmCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "klm"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def cookied_popup(self):
        # for confirming cookies pop-up
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, 'button[id="agreeButton"] span')

            if element:
                element.click()
                logging.info(self.site_name + " :cookies pop-up button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: cookies pop-up button element is not attached to the page document")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: cookies pop-up button element is not attached to the page document")
            # for confirmation code test
        try:
            element = self.driver.find_element(By.ID, "identification")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "identification").clear()

            self.driver.find_element(By.ID, "identification").send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('identification'), 'blur');")

            if "false" in element.get_attribute("aria-invalid"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def flight_carrier_code(self):
        # for flight carrier code test
        try:

            element = self.driver.find_element(By.ID, "carrier")

            if element:
                logging.info(self.site_name + " :flight carrier code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: flight carrier code element is not attached to the page document")

            self.driver.find_element(By.ID, "carrier").send_keys(Testvalues.data["%34$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('carrier'), 'blur');")

            if "false" in element.get_attribute("aria-invalid"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: flight carrier code element is not attached to the page document")

    def flight_number(self):
        # for flight number test
        try:

            element = self.driver.find_element(By.ID, "fltnumber")

            if element:
                logging.info(self.site_name + " :flight carrier code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: flight carrier code element is not attached to the page document")
            self.driver.find_element(By.ID, "fltnumber").clear()

            self.driver.find_element(By.ID, "fltnumber").send_keys(Testvalues.data["%35$@"])

            if "false" in element.get_attribute("aria-invalid"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            pass

    def submit_button(self):
        # submitting form
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'div[id="gotoCheckin"] button[id="gcheckinSubmit"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
            element = self.driver.find_element(By.CSS_SELECTOR,'div[id="identificationError"]')

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        logging.info(self.site_name + " :Desktop Site Tests Finished!!")
