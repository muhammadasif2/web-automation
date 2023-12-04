from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class AustrianAirlinesCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "austrian"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def last_name(self):
        try:   # for confirmation code test
            element = WebDriverWait(
                self.driver,
                5

            ).until(EC.presence_of_element_located((By.ID, 'lastNameEtix')))

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "lastNameEtix").clear()

            self.driver.find_element(By.ID, "lastNameEtix").send_keys(Testvalues.data["%3$@"])
        except Exception:
             logging.error(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def confirmation_code(self):
        # for last name test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, "input[name=\"pnr\"]")

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, "input[name=\"pnr\"]").clear()

            self.driver.find_element(By.CSS_SELECTOR, "input[name=\"pnr\"]").send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting form
            element = WebDriverWait(
                self.driver,
                10

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[id="whereToMain"]')))

            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

            element = WebDriverWait(
                self.driver,
                5

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[class="highlight font-large"]')))

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

            logging.info(self.site_name + " :Desktop Site Tests Finished!!")
