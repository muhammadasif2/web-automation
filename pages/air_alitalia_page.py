from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from  testvalues import  Testvalues


class AiralitaliaCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "Airalitalia"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def confirmation_code(self):
        try:

            # for confirmation code test
            element = WebDriverWait(
                self.driver,
                20

            ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name=\"vcrNumber\"]')))

            if element:
                logging.info(self.site_name + "  :confirmation code field exists")
            else:
                logging.info(self.site_name + "  :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.querySelector('input[name=\"vcrNumber\"]'), 'focus');")

            if "is-focused" in element.find_element_by_xpath("..").get_attribute("class"):
                logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + "  :Assertion mismatch after firing event on input field")
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="vcrNumber"]').clear()

            self.driver.find_element(By.CSS_SELECTOR, 'input[name="vcrNumber"]').send_keys("0551234567891")
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.querySelector('input[name=\"vcrNumber\"]'), 'blur');")
        except Exception:
            logging.error(self.site_name + "  :Assertion mismatch after firing event on input field")

    def last_name(self):

        # for last name test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]')

            if element:
                logging.info(self.site_name + "  :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('input[name=\"lastName\"]'), 'focus');")

            if "is-focused" in element.find_element_by_xpath("..").get_attribute("class"):
                logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + "  :Assertion mismatch after firing event on input field")
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').clear()

            self.driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('input[name=\"lastName\"]'), 'blur');")
        except Exception:
            logging.error(self.site_name + "  :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form

        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'div[id="sbmt-checkin-0"] button[id="sbmt-checkin-0-continue"]')
            if element:
                element.click()
                logging.info(self.site_name + "  :submit button exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: submit button element is not attached to the page document")
            element = WebDriverWait(
                self.driver,
                20

            ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[id="modal-content"]')))
            if element:
                logging.info(self.site_name + "  :error message exists")
            else:
                logging.info(self.site_name + "  :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + "  :Desktop Site Tests Finished!!")

