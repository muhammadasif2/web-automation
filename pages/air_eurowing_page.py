from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class EurowingCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "Eurowing-"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def checkin_tab(self):
            element = WebDriverWait(
                self.driver,
                20

            ).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'li[id="tab1"] a[href="#panel1"]')))
            if element:
                element.click()
                logging.error(self.site_name + " :Checkin tab exit")
        # except Exception:
        #     logging.error(self.site_name + " :Checkin tab is not exit")

    def confirmation_code(self):
        # for confirmation code test


            element = self.driver.find_element(By.ID,"CheckinInfoViewControlGroupCheckinInfo_CheckinInfoViewLoginControlAnonymous_FIRST_INPUT_CONTROL_WebCheckIn")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID,
                                "CheckinInfoViewControlGroupCheckinInfo_CheckinInfoViewLoginControlAnonymous_FIRST_INPUT_CONTROL_WebCheckIn").clear()
            self.driver.find_element(By.ID,"CheckinInfoViewControlGroupCheckinInfo_CheckinInfoViewLoginControlAnonymous_FIRST_INPUT_CONTROL_WebCheckIn").send_keys(
                Testvalues.data["%26$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('CheckinInfoViewControlGroupCheckinInfo_CheckinInfoViewLoginControlAnonymous_FIRST_INPUT_CONTROL_WebCheckIn'), 'blur');")
            if "success" in element.find_element_by_xpath("..").find_element_by_xpath("..").get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        # except Exception:
        #     logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def last_name(self):
        # for last name test
        try:

            element = self.driver.find_element(By.ID,"CheckinInfoViewControlGroupCheckinInfo_CheckinInfoViewLoginControlAnonymous_SECOND_INPUT_CONTROL_WebCheckIn")

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID,"CheckinInfoViewControlGroupCheckinInfo_CheckinInfoViewLoginControlAnonymous_SECOND_INPUT_CONTROL_WebCheckIn").clear()

            self.driver.find_element(By.ID,"CheckinInfoViewControlGroupCheckinInfo_CheckinInfoViewLoginControlAnonymous_SECOND_INPUT_CONTROL_WebCheckIn").send_keys(
                Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('CheckinInfoViewControlGroupCheckinInfo_CheckinInfoViewLoginControlAnonymous_SECOND_INPUT_CONTROL_WebCheckIn'), 'blur');")
            if "success" in element.find_element_by_xpath("..").find_element_by_xpath("..").get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form
        try:

            element = self.driver.find_element(By.CSS_SELECTOR,'button[id="mainSubmitButton"][name="CheckinInfoViewControlGroupCheckinInfo$CheckinInfoViewLoginControlAnonymous$ButtonSubmit"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
            element = self.driver.find_element(By.CSS_SELECTOR, 'div[id="systemErrorMessage"] > p')

            if element:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")


class EurowingCheckinMobilePage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "Eurowing"
        logging.info(self.site_name + "  :Mobile site Tests start")

    def first_name(self):

        # for confirmation code test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[id="recordLocator"]')

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
        except Exception:
            self.failed(
                "Message: stale element reference: confirmation code element is not attached to the page document")
        try:

            self.driver.find_element(By.CSS_SELECTOR, 'input[id="recordLocator"]').clear()
            self.driver.find_element(By.CSS_SELECTOR, 'input[id="recordLocator"]').send_keys(Testvalues.data["%26$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.querySelector('input[id=\"recordLocator\"]'), 'blur');")
            if "valid" in element.find_element_by_xpath("..").get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.info(self.site_name + " :Assertion mismatch after firing event on input field")

    def last_name(self):

        # for last name test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, 'input[id="lastname"]')

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
        try:

            self.driver.find_element(By.CSS_SELECTOR, 'input[id="lastname"]').clear()
            self.driver.find_element(By.CSS_SELECTOR, 'input[id="lastname"]').send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.querySelector('input[id=\"lastname\"]'), 'blur');")
            if "valid" in element.find_element_by_xpath("..").get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.info(self.site_name + " :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form

        element = self.driver.find_element(By.CSS_SELECTOR,'button[data-button="bookingcode"][id="loginViaRecordLocator"]')
        if element:
            self.driver.execute_script(Testvalues.fire_event_script + "document.querySelector('button[data-button=\"bookingcode\"][id=\"loginViaRecordLocator\"]').click();")
            logging.info(self.site_name + " :submit button exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

        WebDriverWait(
            self.driver,
            20

        ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="notificationNoBookingFound"][class~="popup-open"]')))

        if element:
            logging.info(self.site_name + " :error message exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Mobile Site Tests Finished!!")
