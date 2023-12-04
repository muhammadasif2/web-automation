
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from testvalues import Testvalues
import logging


class AirbalticCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "airbaltic"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def checkintab_button(self):

        element = self.driver.find_element_by_link_text('Check-in')
        element.click()

        # self.driver.execute_script(
        #     "document.querySelector('div[data-v-3f783990] a[data-v-3f783990]').click();")

        if element:
            logging.info(self.site_name + " :online check-in tab element exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: online check-in tab element is not attached to the page document")

        try:
            element = self.driver.find_element(By.NAME, "ck_pnr")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

            self.driver.find_element(By.NAME, "ck_pnr").clear()
            self.driver.find_element(By.NAME, "ck_pnr").send_keys('abcdef')
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def last_name(self):

        # for last name test
        try:

            element = self.driver.find_element(By.NAME, 'ck_lastname')

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.NAME, 'ck_lastname').clear()
            self.driver.find_element(By.NAME, 'ck_lastname').send_keys('abc')
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):

        # submitting form
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'form[action*="checkin"] button[type="submit"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
            #  for error Message
            element = WebDriverWait(
                self.driver,
                5

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-v-ff1d3a16][class="texts"] div[data-v-ff1d3a16][class="block ripDescription"]')))

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

            logging.info(self.site_name + " :Desktop Site Tests Finished!!")

