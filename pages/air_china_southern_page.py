from  selenium.webdriver.support.ui import WebDriverWait
from testvalues import Testvalues
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class ChinaSouthernCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "chinasouthern"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def ticket_number(self):

        # for ticket number test
        try:

            element = self.driver.find_element(By.ID, "certificateId")

            if element:
                logging.info(self.site_name + " :ticket number field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: ticket number element is not attached to the page document")
            self.driver.find_element(By.ID, "certificateId").clear()
            self.driver.find_element(By.ID, "certificateId").send_keys(Testvalues.data["%33$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: ticket number element is not attached to the page document")

    def last_name(self):

        # for name test
        try:

            element = self.driver.find_element(By.ID, "guestName")

            if element:
                logging.info(self.site_name + " :name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: name element is not attached to the page document")
            self.driver.find_element(By.ID, "guestName").clear()
            self.driver.find_element(By.ID, "guestName").send_keys(Testvalues.data["%1$@"] + " " + Testvalues.data["%3$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: name element is not attached to the page document")

    def submit_button(self):
        # submitting form
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'form[id="ckiloginForm"] input[type="button"][id="login"]')
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
            element = self.driver.find_element(By.CSS_SELECTOR, 'form[id="ckiloginForm"] ul[id="message-area"] li')

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")
