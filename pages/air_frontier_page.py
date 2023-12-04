from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class FrontierCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "frontier-"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def confirmation_code(self):

        # for confirmation code test
        try:
            element = self.driver.find_element(By.ID, "ConfirmationCode")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "ConfirmationCode").clear()

            self.driver.find_element(By.ID, "ConfirmationCode").send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.info(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def last_namex(self):

        # for last name test
        try:
            element = self.driver.find_element(By.ID, 'passengerLastName')

            if element:
                logging.info(self.site_name + " :last name field exi   sts")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, 'passengerLastName').clear()

            self.driver.find_element(By.ID, 'passengerLastName').send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.info(self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting form
        try:
            element = self.driver.find_element_by_css_selector('div[id="checkIn"] div[class~="divCheckinSearch"] a[id="searchBookingButton"]')

            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        try:
            element = self.driver.find_element_by_css_selector(
                    'form[class="or-msg-alert-error"] div[class="ibe-field-error-img"]')

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

                logging.info(self.site_name + " :Desktop Site Tests Finished!!")

            WebDriverWait(
                self.driver,
                20

            ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.error-msg-alert-error')))
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")


class FrontierCheckinMobilePage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "frontier"
        logging.info(self.site_name + "  :Mobile site Tests start")

    def first_name(self):

        # for confirmation code test

            element = WebDriverWait(
                self.driver,
                20

            ).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#ConfirmationCode')))

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "ConfirmationCode").clear()

            self.driver.find_element(By.ID, "ConfirmationCode").send_keys(Testvalues.data["%26$@"])
        # except Exception:
        #     logging.info(
        #         self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def last_name(self):

        # for confirmation code test
        try:

            element = self.driver.find_element(By.ID, 'passengerLastName')

            if element:
                logging.info(self.site_name + " :last name field exi   sts")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, 'passengerLastName').clear()
            self.driver.find_element(By.ID, 'passengerLastName').send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting form
        element = self.driver.find_element_by_link_text('Check in')
        if element:
            element.click()
            logging.info(self.site_name + " :submit button exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

        # except Exception:
        #     logging.info(
        #         self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

        element = self.driver.find_element_by_css_selector('div[id="checkIn"] div[class~="divCheckinSearch"]')

        if element:
            logging.info(self.site_name + " :error message exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        # except Exception:
        #     logging.info(
        #         self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Mobile Site Tests Finished!!")