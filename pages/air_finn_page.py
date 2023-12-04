from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from testvalues import Testvalues


class FinnAirCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "finnair"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def url_fragment(self):
        # URL fragment test
        try:

            WebDriverWait(
                self.driver,
                100

            ).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'div[class="page-header"]')))
            if EC.url_contains("static/PRD/AY/"):
                logging.info(self.site_name + " :URL fragment exists")
            else:
                logging.info(self.site_name + " :URL fragment is changed!")
        except Exception:
            logging.info(self.site_name + " :URL fragment is changed!")

        # carosal panel heading tab form
        try:
            element = WebDriverWait(
                self.driver,
                20

            ).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'span[id="tab_accordion-group-PNR"][class="panel-heading-tab"]')))
            # element = self.driver.find_element(By.CSS_SELECTOR,'span[id="tab_accordion-group-PNR"][class="panel-heading-tab"]')

            if element:
                element.click()
                logging.info(self.site_name + " :carosal panel heading tab exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: carosal panel heading tab element is not attached to the page document")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: carosal panel heading tab element is not attached to the page document")

    def confirmation_code(self):

        # for confirmation code test
        try:
            element = WebDriverWait(
                self.driver,
                10

            ).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'text-field[model="selection.PNR"] input[name="ssci_text_form_input_1"]')))
            # element = self.driver.find_element(By.CSS_SELECTOR,'text-field[model="selection.PNR"] input[name="ssci_text_form_input_1"]')

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR,
                                'text-field[model="selection.PNR"] input[name="ssci_text_form_input_1"]').clear()

            self.driver.find_element(By.CSS_SELECTOR,'text-field[model="selection.PNR"] input[name="ssci_text_form_input_1"]').send_keys(
                Testvalues.data["%26$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('text-field[model=\"selection.PNR\"] input[name=\"ssci_text_form_input_1\"]'), 'change');")

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

    def last_name(self):

        # for last name test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR,'text-field[model="selection.LastName"] input[name="ssci_text_form_input_0"]')

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR,
                                'text-field[model="selection.LastName"] input[name="ssci_text_form_input_0"]').clear()
            self.driver.find_element(By.CSS_SELECTOR,
                                'text-field[model="selection.LastName"] input[name="ssci_text_form_input_0"]').send_keys(
                Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('text-field[model=\"selection.LastName\"] input[name=\"ssci_text_form_input_0\"]'), 'change');")

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
            
    def submit_button(self):
        # submitting form
        try:
            element =  WebDriverWait(
                    self.driver,
                    200

                ).until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'button[ng-click="click()"]')))
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        except Exception:
                logging.error(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")


        logging.info(self.site_name + " :Desktop Site Tests Finished!!")