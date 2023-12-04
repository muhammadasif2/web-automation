import logging
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from testvalues import Testvalues


class AllnipponCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "allnipponair"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def confirmation_code(self):
        try:
            # for confirmation code test
            element = self.driver.find_element(By.CSS_SELECTOR,'form[action*="checkin"][id="noMemberLogin"] input[id="reservationNumber"]')

            if element:
                logging.info(self.site_name + "  :confirmation code field exists")
            else:
                logging.info(self.site_name + "  :DMessage: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR,
                                'form[action*="checkin"][id="noMemberLogin"] input[id="reservationNumber"]').clear()
            self.driver.find_element(By.CSS_SELECTOR,
                                'form[action*="checkin"][id="noMemberLogin"] input[id="reservationNumber"]').send_keys(
                Testvalues.data["%26$@"])
        except Exception:
             logging.error(set.site_name + "  :DMessage: stale element reference: confirmation code element is not attached to the page document")

    def first_name(self):

        # for First Name test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR,
                                                   'form[action*="checkin"][id="noMemberLogin"] input[id="reservationFirstName"]')

            if element:
                logging.info(self.site_name + "  :first name field exists")
            else:
                logging.info(
                    self.site_name + "  :DMessage: stale element reference: first name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR,'form[action*="checkin"][id="noMemberLogin"] input[id="reservationFirstName"]').clear()

            self.driver.find_element(By.CSS_SELECTOR,
                                'form[action*="checkin"][id="noMemberLogin"] input[id="reservationFirstName"]').send_keys(
                Testvalues.data["%1$@"])
        except Exception:
            logging.error(
                self.site_name + "  :DMessage: stale element reference: first name element is not attached to the page document")

    def last_name(self):
        # for last name test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR,'form[action*="checkin"][id="noMemberLogin"] input[id="reservationLastName"]')

            if element:
                logging.info(self.site_name + "  :Dlast name field exists")
            else:
                logging.info(self.site_name + "  :DMessage: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR,'form[action*="checkin"][id="noMemberLogin"] input[id="reservationLastName"]').clear()
            self.driver.find_element(By.CSS_SELECTOR,'form[action*="checkin"][id="noMemberLogin"] input[id="reservationLastName"]').send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.error(
                self.site_name + "  :DMessage: stale element reference: last name element is not attached to the page document")

    def submit_button(self):
        # submitting form
        try:

            element = self.driver.find_element(By.CSS_SELECTOR,'form[action*="checkin"][id="noMemberLogin"] input[type="submit"][value*="search" i]')
            if element:
                element.click()
                logging.info(self.site_name + "  :Dsubmit button exists")
            else:
                logging.info(
                    self.site_name + "  :DMessage: stale element reference: submit button element is not attached to the page document")
            element = self.driver.find_element(By.CSS_SELECTOR,
                                                   'form[action*="checkin"][name*="ErrorMessageWindow"] div[class~="dialogMessage"]')

            if element:
                logging.info(self.site_name + "  :Derror message exists")
            else:
                logging.info(self.site_name + "  :DMessage: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(self.site_name + "  :DMessage: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + "  :Desktop Site Tests Finished!!")

