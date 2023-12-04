from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from  selenium.webdriver.support.ui import Select
import time


class AirFranceCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "Airfrance"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def popup_button(self):
        # Cookies popup
        try:
            element = self.driver.find_element_by_css_selector(
                    'div[class="gdpr-agree"] button')

            if element:
                element.click()
                logging.info(self.site_name + "  :cookies popup exist")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: check-in tab element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: check-in tab element is not attached to the page document")

    def confirmation_code(self):
        # for confirmation code test

        element = self.driver.find_element_by_id("idIdentNumber")

        if element:
            logging.info(self.site_name + "  :confirmation code field exists")
        else:
            logging.info(
                self.site_name + "  :Message: stale element reference: confirmation code element is not attached to the page document")
        self.driver.find_element_by_id("idIdentNumber").clear()

        self.driver.find_element_by_id("idIdentNumber").send_keys(Testvalues.data['%26$@'])
        self.driver.execute_script(
            Testvalues.fire_event_script + "fireEvent(document.getElementById('idIdentNumber'), 'input');")

        # except Exception:
        #     logging.error(
        #         self.site_name + "  :\Message: stale element reference: confirmation code element is not attached to the page document")
        try:

            if self.driver.find_element_by_css_selector('span[id="idIdentNumber--cleaner"][class="t1__input_cleaner"]'):
                logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + "  :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + "  :Assertion mismatch after firing event on input field")

    def flight_carrer_code(self):
        # for flight carrier code test
        try:

            element = self.driver.find_element(By.ID, "flight_nr_select_id")

            if element:
                logging.info(self.site_name + "  :flight carrier code field exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: flight carrier code element is not attached to the page document")
            self.driver.execute_script(
                Testvalues.fire_event_script + "var letter = 'DL';var selectObj = document.getElementById('flight_nr_select_id');for (var i = 0; i < selectObj.options.length; i++) {if (selectObj.options[i].innerText.toLowerCase() === letter.toLowerCase()) {selectObj.selectedIndex = i;break;}}")
        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: flight carrier code element is not attached to the page document")
        try:

            if self.driver.find_element(By.ID, "flight_nr_select_id").get_attribute("value") == "DL":
                logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + "  :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + "  :Assertion mismatch after firing event on input field")

    def flight_number(self):
        # for flight number test

        try:
            element = self.driver.find_element(By.ID, "idFlight")

            if element:
                logging.info(self.site_name + "  :flight number field exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: flight number element is not attached to the page document")
            self.driver.find_element(By.ID, "idFlight").clear()

            self.driver.find_element(By.ID, "idFlight").send_keys('1234')
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('idFlight'), 'input');")
        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: flight number element is not attached to the page document")
        try:

            if self.driver.find_element_by_css_selector('span[id="idFlight--cleaner"][class="t1__input_cleaner"]'):
                logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + "  :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + "  :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form
        try:

            element = self.driver.find_element(By.CSS_SELECTOR,'form[id="ici_form_resa"][action*="checkin"] button[id="validate_ici_button"]')
            if element:
                element.click()
                logging.info(self.site_name + "  :submit button exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: submit button element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: submit button element is not attached to the page document")

        logging.info(self.site_name + "  :Desktop Site Tests Finished!!")


