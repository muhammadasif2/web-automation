from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from testvalues import Testvalues


class DeltaCheckinMobilePage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "Delta"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def confirmation_code(self):

        # for confirmation code test
        try:
            element = WebDriverWait(
                self.driver,
                30

            ).until(EC.visibility_of_element_located((By.ID, "confirmation_no")))

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.execute_script(Testvalues.fire_event_script + "var letter = '" + Testvalues .data[
                "%26$@"] + "';document.getElementById('confirmation_no').value = letter;")
        except Exception:
            logging.error(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def airport_code(self):

        # for airport code test
        try:
            element = self.driver.find_element(By.ID, "airport_code")

            if element:
                logging.info(self.site_name + " :airport code field exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: airport code element is not attached to the page document")

            self.driver.execute_script(Testvalues.fire_event_script + "var letter = '" + Testvalues.data[
                "%32$@"] + "';document.getElementById('airport_code').value = letter;")
        except Exception:
            logging.error(self.site_name + " :Message: stale element reference: airport code element is not attached to the page document")

    def submit_button(self):
        # submitting form

        element = WebDriverWait(
            self.driver,
            10

        ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[id="find_pnr"]')))

        if element:
            self.driver.execute_script(
                Testvalues.fire_event_script + "document.querySelector('button[id=\"find_pnr\"]').click();")
            logging.info(self.site_name + " :submit button exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

        element = WebDriverWait(
            self.driver,
            10

        ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="ui-dialog"][id="dialog"]')))

        if element:
            logging.info(self.site_name + " :error message exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Mobile Site Tests Finished!!")
