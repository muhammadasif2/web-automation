import logging
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from testvalues import Testvalues


class CatheyPacificChekinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "catheypacific"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def first_name(self):
            # for first name test
            element = WebDriverWait(
                self.driver,
                10

            ).until(EC.presence_of_element_located((By.ID ,'txtGivenName')))

            if element:
                logging.info(self.site_name + " :first name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('txtGivenName'), 'focus');")
            self.driver.find_element(By.ID, "txtGivenName").clear()

            self.driver.find_element(By.ID, "txtGivenName").send_keys(Testvalues.data["%1$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('txtGivenName'), 'input');")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('txtGivenName'), 'blur');")

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")

    def last_name(self):
        # for last name test
            element = self.driver.find_element(By.ID, "txtFamilyName")

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('txtFamilyName'), 'focus');")
            self.driver.find_element(By.ID, "txtFamilyName").clear()

            self.driver.find_element(By.ID, "txtFamilyName").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('txtFamilyName'), 'input');")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('txtFamilyName'), 'blur');")

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")

    def confirmation_code(self):
        try:

            # for confirmation code test
            element = self.driver.find_element(By.ID, "txtBookingRef")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('txtBookingRef'), 'focus');")
            self.driver.find_element(By.ID, "txtBookingRef").clear()
        except Exception:
            logging.error(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
        try:

            self.driver.find_element(By.ID, "txtBookingRef").send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('txtBookingRef'), 'input');")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('txtBookingRef'), 'blur');")

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form
        try:

            element = self.driver.find_element(By.CSS_SELECTOR,
                                          'div[class="booking-reference-group"]+button[class^="button-confirmation"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

        try:
            element = WebDriverWait(
                self.driver,
                10

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="error-message-container"]')))

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")

