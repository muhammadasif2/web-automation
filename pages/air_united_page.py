from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from testvalues import Testvalues


class UnitedAirlinesCheckinMobilePage ():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "united airlines"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def checkin_tab(self):

            element = self.driver.find_element_by_css_selector('li[id~="checkInTab"] h2 div')

            if element:
                self.driver.execute_script(
                    Testvalues.fire_event_script + "document.querySelector('li[id~=\"checkInTab\"] h2 div').click();")
                logging.info(self.site_name + " :clicking check-in tab to make it active")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")

    def confirmation_code(self):

        # for confirmation code test
        try:

            element = self.driver.find_element(By.ID, "flightCheckInConfNumber")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.error(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "flightCheckInConfNumber").clear()

            self.driver.find_element(By.ID, "flightCheckInConfNumber").send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "var element = document.getElementById('flightCheckInConfNumber');var ev = new Event('input', { bubbles: true});ev.simulated = true;element.value = \"abcdef\"; element.defaultValue = \"Something new\";element.dispatchEvent(ev);")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def last_name(self):
        # for last name test
        try:

            element =  self.driver.find_element(By.ID, 'flightCheckInLastName')

            if element:
                logging.info(self.site_name + " :last name field is exist")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, 'flightCheckInLastName').clear()

            self.driver.find_element(By.ID, 'flightCheckInLastName').send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "var element = document.getElementById(\"flightCheckInLastName\");var ev = new Event('input', { bubbles: true});ev.simulated = true;element.value = \"Xyz\";element.defaultValue = \"Something new\";element.dispatchEvent(ev)")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting form

        # submitting form and checking on the error message
        element = self.driver.find_element(By.ID,'formSubmitBtn')
        if element:
            self.driver.execute_script(
                Testvalues.fire_event_script + "document.getElementById('formSubmitBtn').click();")
            logging.info(self.site_name + " :Mobile Site submit button exists")
        else:
            logging.info(self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        element = WebDriverWait(
            self.driver,
            100

        ).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div h1[class="ContentBlueHeder"]')))

        if element and "Flight Check-in" in element.text:
            logging.info(self.site_name + " :error message exists")
        else:
            logging.info(self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Mobile Site Tests Finished!!")
