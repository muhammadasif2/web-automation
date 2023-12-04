from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class KoreanAirCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "koreanair"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def checkin_tab(self):
        # clicking check-in tab
        try:

            element = self.driver.find_element_by_css_selector('dt[class="tab tab-checkin"] a[id="step1-tab2"] span[class="sWrap"]')

            if element:
                element.click()
                logging.info(self.site_name + " :clicking check-in tab to make it active")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")
            time.sleep(1)
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")

        # for confirmation code test
        try:

            element = self.driver.find_element(By.ID, "reservation-number")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "reservation-number").clear()

            self.driver.find_element(By.ID, "reservation-number").send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('reservation-number'), 'keyup');")

        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
        try:

            if "display" in self.driver.find_element(By.ID, "pnrEnterEx1").get_attribute("style"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def first_name(self):
        # for first name test
        try:

            element = self.driver.find_element(By.ID, "reservationFirstName")

            if element:
                logging.info(self.site_name + " :first name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
            self.driver.find_element(By.ID, "reservationFirstName").clear()
            time.sleep(1)
            self.driver.find_element(By.ID, "reservationFirstName").send_keys(Testvalues.data["%1$@"] + " " + Testvalues.data["%2$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('reservationFirstName'), 'keyup');")
            time.sleep(1)
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
        try:

            if "display" in self.driver.find_element(By.ID, "placeholder-reservationFirstNAme").get_attribute("style"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")
            # for confirm checkbox
            try:

                element = self.driver.find_element(By.CSS_SELECTOR,
                                              'div[id="check-in-search"] input[id="nonmem-agree"][type="checkbox"]')
                if element:
                    element.click()
                    logging.info(self.site_name + " :confirm checkbox button exists")
                else:
                    logging.info(
                        self.site_name + " :Message: stale element reference: confirm checkbox button element is not attached to the page document")
            except Exception:
                logging.error(
                    self.site_name + " :Message: stale element reference: confirm checkbox button element is not attached to the page document")

    def last_name(self):
        # for last name test
        try:

            element = self.driver.find_element(By.ID, "reservationLastName")

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, "reservationLastName").clear()

            self.driver.find_element(By.ID, "reservationLastName").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('reservationLastName'), 'keyup');")

        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
        try:

            if "display" in self.driver.find_element(By.ID, "placeholder-reservationLastName").get_attribute("style"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form

        try:
            element = self.driver.find_element(By.CSS_SELECTOR, 'button[id="searchCheckin"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

            element = self.driver.find_element(By.CSS_SELECTOR, 'div[class="confirm-message"] p[class~="msg-txt"]')

            if element and "agree to all policies" in element.text:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")

