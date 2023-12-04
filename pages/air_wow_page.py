from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class WowAirCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "wowair"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def last_name(self):

        # for last name test
        try:

            element = self.driver.find_element(By.ID, 'lastName')

            if element:
                logging.info(self.site_name + " :last name field exi   sts")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, 'lastName').clear()
            time.sleep(1)
            self.driver.find_element(By.ID, 'lastName').send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def confirmation_code(self):
        # for confirmation code test
        try:

            element = self.driver.find_element(By.ID, "confirmationNumber")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "confirmationNumber").clear()

            self.driver.find_element(By.ID, "confirmationNumber").send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def submit_button(self):

        self.driver.execute_script(
            Testvalues.fire_event_script + "document.querySelector('button[type=\"button\"][value=\"Submit\"][onclick*=\"sendInfo\"]').click();")
        element = self.driver.find_element_by_css_selector('button[type="button"][value="Submit"][onclick*="sendInfo"]')
        if element:
            element.click()
            logging.info(self.site_name + " :submit button exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

        try:

            element = self.driver.find_element_by_css_selector('button[type="button"][value="Submit"][onclick*="sendInfo"]')

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:

            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        logging.info(self.site_name + " :Desktop Site Tests Finished!!")