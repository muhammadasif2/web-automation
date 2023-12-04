
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from testvalues import Testvalues
from selenium.common.exceptions import NoSuchElementException


class NorwegianCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "norwegian"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def confirmation_code(self):

        # for confirmation code test
        try:
            element = self.driver.find_element_by_css_selector('input[ng-model="vm.reservation.pnr"]')

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element_by_css_selector('input[ng-model="vm.reservation.pnr"]').clear()

            self.driver.find_element_by_css_selector('input[ng-model="vm.reservation.pnr"]').send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def last_name(self):

        # for last name test
        try:
            element = self.driver.find_element_by_css_selector('input[ng-model="vm.reservation.pnrName"]')

            if element:
                logging.info(self.site_name + " :last name field exi   sts")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element_by_css_selector('input[ng-model="vm.reservation.pnrName"]').clear()

            self.driver.find_element_by_css_selector('input[ng-model="vm.reservation.pnrName"]').send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting for

        element = WebDriverWait(
            self.driver,
            20

        ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-ng-class="buttonModifier"]')))

        if element:
            element.click()
            logging.info(self.site_name + " :submit button exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

        element = WebDriverWait(
            self.driver,
            30

        ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"][data-ng-class="buttonModifier"]')))

        if element:
            logging.info(self.site_name + " :error message exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")