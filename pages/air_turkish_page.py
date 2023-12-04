from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class TurkishAirlinesCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "turkishairlines"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def tab_click(self):

        #clicking check-in tab
            element = WebDriverWait(
                self.driver,
                100

            ).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul[class~="nav"] li a[aria-label~="Check-in"]')))

            if element:
                element.click()
                self.driver.execute_script(Testvalues.fire_event_script + "document.querySelectorAll('ul[class~=\"nav\"] li a[aria-label~=\"Check-in\"]')[0].click();")
                logging.info(self.site_name + " :clicking check-in tab to make it active")
            else:
                logging.info(self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")
        # except Exception:
        #     logging.info(
        #         self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")

    def confirmation_code(self):
        try:
            element = WebDriverWait(
                self.driver,
                100

            ).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '#ticketNo')))

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('ticketNo'), 'focus');")
            element.clear()
            element.send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('ticketNo'), 'input');")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('ticketNo'), 'blur');")

        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def last_name(self):
        # for last name test

        try:

            if self.driver.find_element(By.ID, "surname"):
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('surname'), 'focus');")
            self.driver.find_element(By.ID, "surname").clear()

            self.driver.find_element(By.ID, "surname").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('surname'), 'input');")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('surname'), 'blur');")

        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting form and checking on the error message

        element = self.driver.find_element_by_css_selector('div[id="bookerManageTab"] a[name="submit"][role="button"]')
        if element:
            element.click()
            logging.info(self.site_name + " :submit button exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        element = WebDriverWait(
            self.driver,
            100

        ).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[class="word-wrap"]')))

        if element and "You entered an incorrect or incomplete reservation code (PNR)" in element.text:
            logging.info(self.site_name + " :error message exists")
        else:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")

