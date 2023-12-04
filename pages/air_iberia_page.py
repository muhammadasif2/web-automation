
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from testvalues import Testvalues
import logging


class IberiaCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "Iberia"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def first_last(self):

        # for last name test
        try:

            element = self.driver.find_element(By.ID, "ANONYMOUS_LOGIN_INPUT_SURNAME")

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, "ANONYMOUS_LOGIN_INPUT_SURNAME").clear()
            self.driver.find_element(By.ID, "ANONYMOUS_LOGIN_INPUT_SURNAME").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('ANONYMOUS_LOGIN_INPUT_SURNAME'), 'change');")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
        try:

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.info(self.site_name + " :Assertion mismatch after firing event on input field")

    def confirmation_code(self):

        # for confirmation code test
        try:

            element = self.driver.find_element(By.ID, "ANONYMOUS_LOGIN_INPUT_PNR")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "ANONYMOUS_LOGIN_INPUT_PNR").clear()
            self.driver.find_element(By.ID, "ANONYMOUS_LOGIN_INPUT_PNR").send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(
                self.fire_event_script + "fireEvent(document.getElementById('ANONYMOUS_LOGIN_INPUT_PNR'), 'change');")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
        try:
            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.info(self.site_name + " :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form
        try:
            element =  WebDriverWait(
                self.driver,
                30

            ).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#ANONYMOUS_LOGIN_BOTON')))

            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, 'div[class~="modal-dialog"] p[class~="ib-text"]')

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

            WebDriverWait(
                self.driver,
                40

            ).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#MOD_ERROR_ACCEPT_BUTTON')))
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        logging.info(self.site_name + " :Desktop Site Tests Finished!!")