
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from testvalues import Testvalues
import logging


class JapanAirlinesCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "japanairlines"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def click_tab(self):
        try:

            element = WebDriverWait(
                self.driver,
                20

            ).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#tab_accordion-group-ETKT')))
            element.click()
        except Exception:
            logging.error(
                self.site_name + " :tab button is not exist")

    def confirmation_code(self):
        try:

            # for confirmation code test

            element = WebDriverWait(
                self.driver,
                10

            ).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input[name="ssci_text_form_input_3"]')))

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="ssci_text_form_input_3"]').clear()

            self.driver.find_element(By.CSS_SELECTOR, 'input[name="ssci_text_form_input_3"]').send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('input[name=\"ssci_text_form_input_3\"]'), 'change');")

        except Exception:
            logging.error(self.site_name +
                " :Message: stale element reference: confirmation code element is not attached to the page document")
        try:

            if "ng-invalid" in self.driver.find_element(By.CSS_SELECTOR, 'input[id="form_input_0"]').get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.error(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def last_name(self):
        # for last name test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="ssci_text_form_input_4"]')
            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="ssci_text_form_input_4"]').clear()

            self.driver.find_element(By.CSS_SELECTOR, 'input[name="ssci_text_form_input_4"]').send_keys(
                Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('input[name=\"ssci_text_form_input_4\"]'), 'change');")

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.error(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def first_name(self):
        # for first name test

        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="ssci_text_form_input_5"]')

            if element:
                logging.info(self.site_name + " :first name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="ssci_text_form_input_5"]').clear()

            self.driver.find_element(By.CSS_SELECTOR, 'input[name="ssci_text_form_input_5"]').send_keys(
                Testvalues.data["%1$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('input[name=\"ssci_text_form_input_5\"]'), 'change');")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
        try:

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.error(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def fligh_number(self):
        # for flight number test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="flight_number_ETKT"]')

            if element:
                logging.info(self.site_name + " :flight number field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: flight number element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="flight_number_ETKT"]').clear()

            self.driver.find_element(By.CSS_SELECTOR, 'input[name="flight_number_ETKT"]').send_keys(
                Testvalues.data["%35$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('input[ng-model=\"selection.FlightNumber.number\"]'), 'change');")

        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: flight number element is not attached to the page document")
        try:

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.error(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form
        try:

            element = self.driver.find_element(By.CSS_SELECTOR,
                                          'form[name="identification_PNR"] navigation-group-buttons[ssci-id="navigationGroupId"] button[id="buttonId_0_0"]')
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
            element = self.driver.find_element(By.CSS_SELECTOR,'div[id="messages-page-header"] span[translate="Message.NoPassengersFoundTitle"]')

            if element and "No Passenger Found" in element.text:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.error(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")
