import logging
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from testvalues import Testvalues


class AmericanArilinesCheckinPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "americanarilines"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def first_name(self):
        try:

            # for First name test
            element = self.driver.find_element(By.ID, "findReservationForm.firstName")

            if element:
                logging.info(self.site_name + " :first name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
            self.driver.find_element(By.ID, "findReservationForm.firstName").clear()
            self.driver.find_element(By.ID, "findReservationForm.firstName").send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: first name element is not attached to the page document")

    def last_nam(self):

        # for last name test


            element = self.driver.find_element(By.ID, "findReservationForm.lastName")

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, "findReservationForm.lastName").clear()

            self.driver.find_element(By.ID, "findReservationForm.lastName").send_keys(Testvalues.data["%3$@"])
        # except Exception:
        #     logging.error(
        #         self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def confirmation_code(self):
        # for confirmation code test
        try:

            element =  self.driver.find_element(By.ID, "findReservationForm.recordLocator")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "findReservationForm.recordLocator").clear()

            self.driver.find_element(By.ID, "findReservationForm.recordLocator").send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.error(
                self.self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def submit_button(self):
        # submitting form
        try:

            element = self.driver.find_element(By.ID, 'findReservationForm.submit')
            if element:
                self.driver.execute_script(
                    Testvalues.fire_event_script + "document.getElementById('findReservationForm.submit').click();")
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
            element = self.driver.find_element(By.ID, 'globalErrors.errors')

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")
