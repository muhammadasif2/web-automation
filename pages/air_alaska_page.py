from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class AlaskaAirCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "alaskaairlines"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def checkin_city(self):

        try:
            element =  self.driver.find_element(By.ID, "FindReservation_Departure")

            if element:
                logging.info(self.site_name + "  :check-in city field exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: check-in city element is not attached to the page document")
            self.driver.find_element(By.ID, "FindReservation_Departure").send_keys('LAS')
            self.driver.execute_script( Testvalues.fire_event_script + "fireEvent(document.getElementById('FindReservation_Departure'), 'change');")

        except Exception:
            logging.error(self.site_name + "  :Message: stale element reference: check-in city element is not attached to the page document")
        try:
            if "FindReservationDepart_DrpList" not in self.driver.find_element(By.ID, "FindReservation_Departure").get_attribute("class"):
                logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + "  :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + "  :Assertion mismatch after firing event on input field")
        try:

            element = self.driver.find_element(By.ID, "FindReservation_LookupOptions")

            if element:
                logging.info(self.site_name + "  :how to look up your reservation' field exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: 'how to look up your reservation' element is not attached to the page document")
            self.driver.find_element(By.ID, "FindReservation_LookupOptions").send_keys("Confirmation")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('FindReservation_LookupOptions'), 'change');")
        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: 'how to look up your reservation' element is not attached to the page document")

    def last_name(self):
        # for confirmation code test
        try:
            element = self.driver.find_element(By.ID, "FindReservation_Confirmation")

            if element:
                logging.info(self.site_name + "  :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "FindReservation_Confirmation").clear()
            self.driver.find_element(By.ID, "FindReservation_Confirmation").send_keys('abcdef')
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('FindReservation_Confirmation'), 'change');")
        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: confirmation code element is not attached to the page document")

    def submit_button(self):
        # submitting form

        element = self.driver.find_element(By.ID, "FindReservation_Find")
        if element:
            element.click()
            logging.info(self.site_name + "  :submit button exists")
        else:
            logging.info(
                self.site_name + "  :Message: stale element reference: submit button element is not attached to the page document")

        logging.info(self.site_name + "  :Desktop site Tests finished")


