from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from testvalues import  Testvalues


class AeromexicoCheckinDesktopPagae():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "aeromexico"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def confirmation_code(self):

        # for confirmation code test
        try:

            element =  self.driver.find_element_by_id("ticketNumber")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element_by_id("ticketNumber").clear()

            self.driver.find_element_by_id("ticketNumber").send_keys("ahahaa")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('ticketNumber'), 'blur');")

        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
        try:

            if self.driver.find_element_by_css_selector('input[id="ticketNumber"]+span[class~="FormInput-correct"]'):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def last_name(self):

        # for last name test
        try:

            if self.driver.find_element(By.ID, "lastName"):
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, "lastName").clear()
            self.driver.find_element(By.ID, "lastName").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('lastName'), 'blur');")

        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
        try:

            if self.driver.find_element_by_css_selector('input[id="lastName"]+span[class~="FormInput-correct"]'):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form and checking on the error message
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'div[class$="PNRLookupForm-submit"] button[type="submit"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
            element = WebDriverWait(
                self.driver,
                30

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR,'p[class="ErrorBar-description"]')))

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")