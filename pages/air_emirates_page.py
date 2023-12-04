from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class EmiratesCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "emirates-"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def checkin_tab(self):
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'li[id="tab1"] a[href="#panel1"]')
            element.click()
        except Exception:
            logging.error(self.site_name + " :Checkin Tab is not exist")

    def confirmation_code(self):
        # for confirmation code test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').clear()

            self.driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def last_name(self):

        # for last name test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="ref-id"]')

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="ref-id"]').clear()

            self.driver.find_element(By.CSS_SELECTOR, 'input[name="ref-id"]').send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        try:

            # submitting form
            element = WebDriverWait(
                self.driver,
                20

            ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="grid__item medium--one-quarter my-trips__cta"] button[class~="js-my-trips-submit-check-in"] span[class~="cta__text"]')))
            # element = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"] span[class~="cta__text"]')
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

            element =self.driver.find_element(By.CSS_SELECTOR,'div[class~="errorPanel"] input[id*="hdnServerError"]')

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")
        WebDriverWait(
            self.driver,
            20

        ).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#sHLErrorsText')))


class EmiratesCheckinMobilePage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "emirates"
        logging.info(self.site_name + "  :Mobile site Tests start")

    def last_name(self):

        # for last name test
        try:

            element = self.driver.find_element(By.ID, "lastName")

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, "lastName").clear()
            self.driver.find_element(By.ID, "lastName").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('lastName'), 'keyup');")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('lastName'), 'blur');")
        except Exception:
            logging.error(self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
        try:

            if "validated" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def confirmation_code(self):

        # for confirmation code test
        try:

            element = self.driver.find_element(By.ID, "bookingRef")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(self.self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "bookingRef").clear()
            self.driver.find_element(By.ID, "bookingRef").send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('bookingRef'), 'keyup');")

            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('bookingRef'), 'blur');")

        except Exception:
            logging.error(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
        try:

            if "validated" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def submit_button(self):
        try:

            # submitting form

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[id="olci_Login_submitBtn"][type="submit"]')
            if element:
                self.driver.execute_script(Testvalues.fire_event_script + "document.querySelector('input[id=\"olci_Login_submitBtn\"][type=\"submit\"]').click();")
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

        except Exception:
            logging.error(self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

        try:
            element = self.driver.find_element(By.CSS_SELECTOR, 'div[id="olciLoginTab"] div[class~="popup-error-band"]')

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Mobile Site Tests Finished!!")
        # WebDriverWait(
        #     self.driver,
        #     20
        #
        # ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#errorPage_bokFlt')))