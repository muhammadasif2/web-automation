from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class RyanAirCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "ryanair"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def confirmation_code(self):
        # for confirmation code test
        try:
            element = WebDriverWait(
                self.driver,
                10

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[ng-model="myTrips.info.reservationNum"]')))

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element_by_css_selector('input[ng-model="myTrips.info.reservationNum"]').clear()

            self.driver.find_element_by_css_selector('input[ng-model="myTrips.info.reservationNum"]').send_keys(
                Testvalues.data["%26$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
        # for Email test
        try:

            element = self.driver.find_element_by_css_selector('input[ng-model="myTrips.info.email"]')

            if element:
                logging.info(self.site_name + " :email field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element_by_css_selector('input[ng-model="myTrips.info.email"]').clear()

            self.driver.find_element_by_css_selector('input[ng-model="myTrips.info.email"]').send_keys(
                Testvalues.data["%11$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def email_test(self):

        # for Email test
        try:

            element = self.driver.find_element_by_css_selector('input[ng-model="myTrips.info.email"]')

            if element:
                logging.info(self.site_name + " :email field exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element_by_css_selector('input[ng-model="myTrips.info.email"]').clear()

            self.driver.find_element_by_css_selector('input[ng-model="myTrips.info.email"]').send_keys(Testvalues.data["%11$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting form
        try:

            element = self.driver.find_element_by_css_selector('button[translate="trips.my_trips.go"][type="submit"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
            WebDriverWait(
                self.driver,
                10

            ).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span[class="error"]')))
            element = WebDriverWait(
                self.driver,
                10

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[translate="trips.my_trips.go"][type="submit"]')))

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
            WebDriverWait(
                self.driver,
                10

            ).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span[class="error"]')))
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")


class RyanAirCheckinMobilePage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "ryanair"
        logging.info(self.site_name + "  :Mobile site Tests start")

    def confirmation_code(self):
        try:

            # for confirmation code test
            element = self.driver.find_element(By.ID, "ByEmailAddress_ReservationNumber")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "ByEmailAddress_ReservationNumber").clear()

            self.driver.find_element(By.ID, "ByEmailAddress_ReservationNumber").send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('ByEmailAddress_ReservationNumber'), 'change');")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def email_test(self):
        # for Email test
        try:

            element = self.driver.find_element(By.ID, 'ByEmailAddress_EmailAddress')

            if element:
                logging.info(self.site_name + " :email field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, 'ByEmailAddress_EmailAddress').clear()

            self.driver.find_element(By.ID, 'ByEmailAddress_EmailAddress').send_keys(Testvalues.data["%11$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        try:

            # submitting form and checking on the error message
            element = self.driver.find_element_by_css_selector('button[class="btn btn-primary btn-block pull-right retrieve"]')
            if element:
                element.click()
                logging.info(self.site_name + " :Mobile Site submit button exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        logging.info(self.site_name + " :Mobile Site Tests Finished!!")