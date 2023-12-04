import logging
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from testvalues import Testvalues


class BritishAirCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "british Airlines"
        logging.info(self.site_name + "  :Desktop site Tests start")
        self.wait = WebDriverWait(
            self.driver,
            30)

    def confirmation_code(self):

        # for confirmation code test

        try:
            element = self.driver.find_element(By.ID, "bookingRef")

            if element:
                logging.info(self.site_name + "  :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "bookingRef").clear()

            self.driver.find_element(By.ID, "bookingRef").send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('bookingRef'), 'blur');")

            if "false" in element.get_attribute("aria-invalid"):
                logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + "  :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: confirmation code element is not attached to the page document")

    def last_name(self):

        # for last name test
        try:

            element = self.driver.find_element(By.ID, "lastname")

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, "lastname").clear()

            self.driver.find_element(By.ID, "lastname").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('lastname'), 'blur');")

            if "false" in element.get_attribute("aria-invalid"):
                logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + "  :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + "  :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form

        element = self.driver.find_element(By.CSS_SELECTOR,
                                      'form[action*="managebooking"] input[type="submit"][title~="check-in"]')
        if element:
            element.click()
            logging.info(self.site_name + " :submit button exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        element = WebDriverWait(
            self.driver,
            10

        ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id="mfErrorsOne"]')))

        if element and "unable to find your booking" in element.text:
            logging.info(self.site_name + " :error message exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")