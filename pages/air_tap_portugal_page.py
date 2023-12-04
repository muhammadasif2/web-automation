from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class TapPortugalCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "tapPortugal"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def tab_click(self):

        # clicking check-in tab
        element = WebDriverWait(
            self.driver,
            100

        ).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[id="tab_accordion-group-PNR"]')))

        if element:
            element.click()
            logging.info(self.site_name + " :clicking check-in tab to make it active")
        else:
            logging.info(self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")

    def confirmation_code(self):
        # for confirmation code test
        try:

            element = self.driver.find_element_by_css_selector('input[ng-model="ngModel')

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element_by_css_selector('input[ng-model="ngModel"]').clear()

            self.driver.find_element_by_css_selector('input[ng-model="ngModel').send_keys(Testvalues.data["%26$@"])
        except Exception:
            self.failed(
                "Message: stale element reference: confirmation code element is not attached to the page document")

    def last_name(self):
        # for departure date test
        try:

            element = self.driver.find_element_by_css_selector('select[ng-model="selection.DepartureDate"]')

            if element:
                logging.info(self.site_name + " :departure date field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: departure date element is not attached to the page document")

            self.driver.find_element_by_css_selector('select[ng-model="selection.DepartureDate"]').send_keys(
                Testvalues.data["%40$@"] + "-" + Testvalues.data["%38$@"] + "-" + Testvalues.data["%39$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('departure_date_PNR'), 'keyup');")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: departure date element is not attached to the page document")

    def submit_button(self):
        # submitting form
        try:

            element = self.driver.find_element_by_css_selector('span[translate="NavigationOption.Identify"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        except Exception:

            element = self.driver.find_element_by_css_selector('span[translate="NavigationOption.Identify"]')

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

            WebDriverWait(
                self.driver,
                30

            ).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[translate="Message.NoPassengersFoundDescription"]')))
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")