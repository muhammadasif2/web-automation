from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from testvalues import Testvalues


class EasyjetCheckinMobilePage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "easyjet"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def Passenger_radio_button(self):

        # passenger booking radio button test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][id="PassengerSignInOption"]')
            if element:
                self.driver.execute_script(
                    Testvalues.fire_event_script + "document.querySelector('input[type=\"radio\"][id=\"PassengerSignInOption\"]').click();")
                logging.info(self.site_name + " :passenger booking radio button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: passenger booking radio button element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: passenger booking radio button element is not attached to the page document")

    def confirmation_code(self):
        try:

            # for confirmation code test

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[ng-model="BookingReference"]')

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

            self.driver.find_element(By.CSS_SELECTOR, 'input[ng-model="BookingReference"]').send_keys(
                Testvalues.data["%26$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('input[ng-model=\"BookingReference\"]'), 'change');")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
        try:

            if "ng-valid" in element.get_attribute("class"):

                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def last_name(self):

        # for last name test

        element = self.driver.find_element(By.CSS_SELECTOR, 'input[ng-model="Surname"]')

        if element:
            logging.info(self.site_name + " :last name field exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-model="Surname"]').clear()

        self.driver.find_element(By.CSS_SELECTOR, 'input[ng-model="Surname"]').send_keys(Testvalues.data["%3$@"])
        self.driver.execute_script(
            Testvalues.fire_event_script + "fireEvent(document.querySelector('input[ng-model=\"Surname\"]'), 'change');")

        try:

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # confirm permission checkbox test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[id="PermissionCheckbox"][type="checkbox"]')
            if element:
                self.driver.execute_script("document.querySelector('input[id=\"PermissionCheckbox\"][type=\"checkbox\"]').click();")
                logging.info(self.site_name + " :confirm permission checkbox exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirm permission checkbox element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: confirm permission checkbox element is not attached to the page document")
        # submitting form
        try:
            element = WebDriverWait(
                self.driver,
                30

            ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="submit"][id="passenger-sign-in-login"]')))

            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
            element = self.driver.find_element(By.CSS_SELECTOR, 'div[ng-show="ShowErrorMessage"]')

            if element and "ng-hide" in element.get_attribute("class"):
                logging.info(self.site_name + " :error message exists")
            else:
                logging.error(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

            WebDriverWait(
                self.driver,
                5

            ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message")))
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        logging.info(self.site_name + " :Mobile Site Tests Finished!!")
