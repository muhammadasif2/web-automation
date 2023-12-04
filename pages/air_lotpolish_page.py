from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class LotPolishCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "lotpolish"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def tab_click(self):
        try:

            element = WebDriverWait(
                self.driver,
                100

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tab_accordion-group-PNR')))
            if element:
               element.click()
            logging.info(self.site_name + " :Message: checkin tab is exist")
        except Exception:
            logging.info(self.site_name + " :Message: checkin tab is not exist")

    def last_name(self):

        # for last name test
        try:

            element = WebDriverWait(
                self.driver,
                100

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'text-field[model="selection.LastName"] input')))

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, 'text-field[model="selection.LastName"] input').clear()
            time.sleep(1)

            self.driver.find_element(By.CSS_SELECTOR, 'text-field[model="selection.LastName"] input').send_keys(
                Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('text-field[model=\"selection.LastName\"] input'), 'change');")
            time.sleep(1)
        except Exception:
            logging.info(self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
        try:

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.info(self.site_name + " :Assertion mismatch after firing event on input field")

    def confirmation_code(self):
        # for confirmation code test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'text-field[model="selection.PNR"] input')

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                self.failed(
                    "Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR, 'text-field[model="selection.PNR"] input').clear()
            time.sleep(1)

            self.driver.find_element(By.CSS_SELECTOR, 'text-field[model="selection.PNR"] input').send_keys(
                Testvalues.data["%26$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('text-field[model=\"selection.PNR\"] input'), 'change');")
            time.sleep(1)
        except Exception:
            logging.error(
                "Message: stale element reference: confirmation code element is not attached to the page document")
        try:

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.info(self.site_name + " :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form
        try:

            element = self.driver.find_element(By.CSS_SELECTOR,'form[name="identification_PNR"] navigation-group-buttons[ssci-id="navigationGroupId"] button[id="buttonId_0_0"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                self.failed(
                    "Message: stale element reference: submit button element is not attached to the page document")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        try:

            element = self.driver.find_element(By.CSS_SELECTOR,'div[id="messages-page-header"] span[translate="Message.NoPassengersFoundTitle"]')

            if element and "No Passengers Found" in element.text:
                logging.info(self.site_name + " :error message exists")
            else:
                self.failed(
                    "Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        logging.info(self.site_name + " :Desktop Site Tests Finished!!")
        element = WebDriverWait(
            self.driver,
            40

        ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[translate = "Message.Error"]')))



