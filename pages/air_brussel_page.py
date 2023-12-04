from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from testvalues import Testvalues


class BrusselAirlinesCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "brusselairlines"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def confirmation_code(self):

        # # for confirmation code test
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, 'input[id*="txtCriteriaValue"]')

            if element:
                logging.info(self.site_name + " confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, 'input[id*="txtCriteriaValue"]').clear()

            self.driver.find_element(By.CSS_SELECTOR, 'input[id*="txtCriteriaValue"]').send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.error(
                self.site_name + " Message: stale element reference: confirmation code element is not attached to the page document")

    def last_name(self):

        # for last name test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[id*="txtLastName"]')

            if element:
                logging.info(self.site_name + " last name field exists")
            else:
                logging.info(
                    self.site_name + "Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, 'input[id*="txtLastName"]').clear()

            self.driver.find_element(By.CSS_SELECTOR, 'input[id*="txtLastName"]').send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.error(
                self.site_name + "Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting form

        try:
            element = self.driver.find_element_by_css_selector('div[id="content"] input[type="submit"][id="ctl00_cplhLevelOne_btnNext_Query"][class="TwoButtonStyle"]')
            if element:
                self.driver.find_element(By.CSS_SELECTOR,'div[id="content"] input[type="submit"][id="ctl00_cplhLevelOne_btnNext_Query"][class="TwoButtonStyle"]').is_displayed()
                self.driver.find_element_by_id("ctl00_cplhLevelOne_btnNext_Query").click()

                logging.info(self.site_name + " submit button exists")
            else:
                logging.info(
                    self.site_name + " Message: stale element reference: submit button element is not attached to the page document")

        except Exception:
            logging.error(self.site_name + " Message: stale element reference: submit button element is not attached to the page document")

    #  for error Message


        try:

            element = self.driver.find_element_by_css_selector('div[class="innercontent"] div[id="ctl00_pnlError"] ul li')

            print(element.text)
            if element and "Web check-in is possible as from 24 hours before departure" in element.text:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")
