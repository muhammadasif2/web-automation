from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from testvalues import Testvalues
import logging


class AireuropaCheckinMobilePage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "aireuropa"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def tocket_number(self):

        # for ticket number test

        element = WebDriverWait(
            self.driver,
            100

        ).until(EC.visibility_of_element_located((By.NAME, 'ticketNumber')))


        if element:
            logging.info(self.site_name + "  :confirmation code field exists")
        else:
            logging.info(
                self.site_name + "  :Message: stale element reference: confirmation code element is not attached to the page document")
        self.driver.execute_script(
            Testvalues.fire_event_script + "fireEvent(document.getElementsByName('ticketNumber')[0], 'focus');")

        # except Exception:
        #     logging.error(
        #         self.site_name + "  :Message: stale element reference: confirmation code element is not attached to the page document")

        try:

            if "display: none" not in self.driver.find_element_by_css_selector(
                    'div[class~="tag-ticketNumber"] div[class~="js_hint_message"]').get_attribute("style"):
                logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
            else:
                self.failed("Assertion mismatch after firing event on input field")
            self.driver.find_element_by_name("ticketNumber").clear()

            self.driver.find_element_by_name("ticketNumber").send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementsByName('ticketNumber')[0], 'input');")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementsByName('ticketNumber')[0], 'blur');")
        except Exception:
            logging.error(self.site_name + "  :Assertion mismatch after firing event on input field")

    def last_name(self):

        # for last name test
        try:

            element =self.driver.find_element_by_name("surname")

            if element:
                logging.info(self.site_name + "  :last name field exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: last name element is not attached to the page document")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementsByName('surname')[0], 'focus');")
            self.driver.find_element_by_name("surname").clear()

            self.driver.find_element_by_name("surname").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementsByName('surname')[0], 'input');")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementsByName('surname')[0], 'blur');")
        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting form and checking on the error message

        element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="search"]')
        if element:
            self.driver.execute_script(
                Testvalues.fire_event_script + "document.querySelector('input[name=\"search\"]'). click();")
            logging.info(self.site_name + "  :submit button exists")
        else:
            logging.info(
                self.site_name + "  :Message: stale element reference: submit button element is not attached to the page document")
        WebDriverWait(
            self.driver,
            20

        ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'article[id="checkin-search"] p[class*="top-error-message"]')))

        if element:
            logging.info(self.site_name + "  :error message exists")
        else:
            logging.info(
                self.site_name + "  :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + "  :Mobile Site Tests Finished!!")