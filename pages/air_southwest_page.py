from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class SouthWestCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "southwest"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def confirmation_code(self):

        # for confirmation code test

        element = self.driver.find_element_by_id("confirmationNumber")

        if element:
            logging.info(self.site_name + " :confirmation code field exists")
        else:
            logging.info(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
        self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('confirmationNumber'), 'focus');")
        self.driver.find_element_by_id("confirmationNumber").clear()
        self.driver.find_element_by_id("confirmationNumber").send_keys(Testvalues.data["%26$@"])
        self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('confirmationNumber'), 'input');")
        self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('confirmationNumber'), 'blur');")
        #
        # except Exception:
        #     logging.error(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def first_name(self):
        # for first name test


            if self.driver.find_element(By.ID, "passengerFirstName"):
                logging.info(self.site_name + " :first name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('passengerFirstName'), 'focus');")
            self.driver.find_element(By.ID, "passengerFirstName").clear()

            self.driver.find_element(By.ID, "passengerFirstName").send_keys(Testvalues.data["%1$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('passengerFirstName'), 'input');")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('passengerFirstName'), 'blur');")

        # except Exception:
        #     logging.error(
        #         self.site_name + " :Message: stale element reference: first name element is not attached to the page document")

    def last_name(self):
        # for last name test
        # try:

            if self.driver.find_element(By.ID, "passengerLastName"):
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('passengerLastName'), 'focus');")
            self.driver.find_element(By.ID, "passengerLastName").clear()

            self.driver.find_element(By.ID, "passengerLastName").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('passengerLastName'), 'input');")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('passengerLastName'), 'blur');")

        # except Exception:
        #     logging.error(
        #         self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting form and checking on the error message
        try:

            element = self.driver.find_element_by_css_selector(
                'div[class~="form-container--search-block"] button[type~="button"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        # element = wait.until(
        #     lambda self.driver: self.driver.find_element(By.CSS_SELECTOR, 'div[class~="ErrorModal"] div[class~="ErrorModal-body"]')
        # )
        # time.sleep(1)
        # if element and "find your reservation" in element.text:
        #     logging.info(self.site_name + " :error message exists")
        # else:
        #     logging.info(self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")
        WebDriverWait(
            self.driver,
            30

        ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[class="page-error--message"]')))


class SouthWestCheckinMobilePage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "southwest"
        logging.info(self.site_name + "  :Mobile site Tests start")

    def confirmation_code(self):

        # for confirmation code test
        try:
            WebDriverWait(
                self.driver,
                30

            ).until(EC.presence_of_element_located(
                (By.NAME, 'recordLocator')))

            element = self.driver.find_element(By.NAME, "recordLocator")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.NAME, "recordLocator").clear()

            self.driver.find_element(By.NAME, "recordLocator").send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementsByName('recordLocator')[0], 'change');")
        except Exception:
            logging.error(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def first_name(self):
        # for first name test

        try:

            if self.driver.find_element(By.NAME, "firstName"):
                logging.info(self.site_name + " :first name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementsByName('firstName')[0], 'focus');")
            self.driver.find_element(By.NAME, "firstName").clear()

            self.driver.find_element(By.NAME, "firstName").send_keys(Testvalues.data["%1$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementsByName('firstName')[0], 'input');")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementsByName('firstName')[0], 'blur');")

        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: first name element is not attached to the page document")

    def last_name(self):
        # for last name test
        try:

            if self.driver.find_element(By.NAME, "lastName"):
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementsByName('lastName')[0], 'focus');")
            self.driver.find_element(By.NAME, "lastName").clear()

            self.driver.find_element(By.NAME, "lastName").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementsByName('lastName')[0], 'input');")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementsByName('lastName')[0], 'blur');")

        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting form and checking on the error message
        try:

            element = self.driver.find_element_by_css_selector('button[class="button button--fluid large button--yellow"]')
            if element:
                element.click()
                logging.info(self.site_name + " :Mobile Site submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        # element = wait.until(
        #     lambda self.driver: self.driver.find_element(By.CSS_SELECTOR, 'div[class~="ErrorModal"] div[class~="ErrorModal-body"]')
        # )
        # time.sleep(1)
        # if element and "find your reservation" in element.text:
        #     logging.info(self.site_name + " :error message exists")
        # else:
        #     logging.info(self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Mobile Site Tests Finished!!")
        WebDriverWait(
            self.driver,
            30

        ).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.popup-title')))