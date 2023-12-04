from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class SasCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "sas"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def click_tab(self):
        # clicking check-in tab
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, '#nav-checkin a[aria-label="Check in"]')

            if element:
                element.click()
                logging.info(self.site_name + " :clicking check-in tab to make it active")
                logging.info(self.site_name + " :Checkin Button is exist")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")

        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")

    def confirmation_code(self):

        # for confirmation code test
        try:

            element = self.driver.find_element(By.ID, "Name")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "Name").clear()

            self.driver.find_element(By.ID, "Name").send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def email_test(self):

        # for last name test
        try:

            element = self.driver.find_element(By.ID, 'lastName')

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, 'lastName').clear()
            self.driver.find_element(By.ID, 'lastName').send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        try:

            element = self.driver.find_element_by_css_selector('div[class="search-btn-wrap"] button[id~="CheckinSearchBtn"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

            element = WebDriverWait(
                self.driver,
                40

            ).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'p[id="notificationMessage"]')))

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")


class SasCheckinMobilePage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "sas"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def last_name(self):

        # for last name test
        try:
            element = self.driver.find_element(By.ID, "txtDefaultLastName")

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('txtDefaultLastName'), 'focus');")
            self.driver.find_element(By.ID, "txtDefaultLastName").clear()

            self.driver.find_element(By.ID, "txtDefaultLastName").send_keys(Testvalues.data["%3$@"])

            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('txtSearchCriteria'), 'change');")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def confirmation_code(self):
        # for confirmation code test
        try:

            element = self.driver.find_element(By.ID, "txtSearchCriteria")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "txtSearchCriteria").clear()
            self.driver.find_element(By.ID, "txtSearchCriteria").send_keys('BWWBBW')
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('txtSearchCriteria'), 'change');")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def submit_button(self):

        # submitting form and checking on the error message
        try:

            element = self.driver.find_element_by_css_selector('div[class="txt"]')
            if element:
                self.driver.execute_script(Testvalues.fire_event_script + "document.querySelector('div[class=\"txt\"]').click();")
                logging.info(self.site_name + " :Mobile Site submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
            element = WebDriverWait(
                self.driver,
                40

            ).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'span[id="myError_lblErrorMessage"]')))

            if element and "Booking not found " in element.text:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Mobile Site Tests Finished!!")