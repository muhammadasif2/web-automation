
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from  testvalues import Testvalues
import logging


class AirCanadaChekinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "aircanada"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def language_pop_up(self):

        # select language pop-up
        try:
            element = WebDriverWait(
                self.driver,
                20

            ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-ng-click="SiteSelectionEdition();"]')))
            # element = self.driver.find_element_by_id("enUSEdition")

            if element:
                element.click()
                logging.info(self.site_name + " :Selecting english language through 'select language pop-up'")

        except Exception:
            logging.error(self.site_name + " :Selecting english language through 'select language pop-up'")
        try:

            # check in tab
            element =  self.driver.find_element_by_css_selector('div[id="tabs_magnet"] span[class~="ac-tab-checkin"]')

            if element:
                element.click()
                logging.info(self.site_name + " :clicking check-in tab to make it active")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")

        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")

    def checkintab_button(self):
        try:
            # check in tab
            element = self.driver.find_element_by_css_selector('div[id="tabs_magnet"] span[class~="ac-tab-checkin"]')

            if element:
                element.click()
                logging.info(self.site_name + " :clicking check-in tab to make it active")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")

        except Exception:
            logging.error(self.site_name + " :Message: stale element reference: check-in tab element is not attached to the page document")

    def first_name(self):
        # first name tests
        try:

            if self.driver.find_element(By.ID, "checkin_first_name"):
                logging.info(self.site_name + " :first name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('checkin_first_name'), 'focus');")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
        try:

            self.driver.find_element(By.ID, "checkin_first_name").clear()

            self.driver.find_element(By.ID, "checkin_first_name").send_keys(Testvalues.data["%1$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('checkin_first_name'), 'input');")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('checkin_first_name'), 'blur');")

            if self.driver.find_element_by_css_selector('input[id="checkin_first_name"][class~="ng-touched"]'):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def last_name(self):
        # Last name
        try:

            if self.driver.find_element(By.ID, "checkin_last_name"):
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('checkin_last_name'), 'focus');")
            self.driver.find_element(By.ID, "checkin_last_name").clear()

            self.driver.find_element(By.ID, "checkin_last_name").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('checkin_last_name'), 'input');")
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('checkin_last_name'), 'blur');")

        except Exception:
            logging.error(self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def confirmation_code(self):

        # confirmation filed

        element = self.driver.find_element_by_id("checkin_aeroplan_or_pnr")

        if element:
            logging.info(self.site_name + " :confirmation code field exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
        self.driver.execute_script(
            Testvalues.fire_event_script + "fireEvent(document.getElementById('checkin_aeroplan_or_pnr'), 'focus');")
        self.driver.find_element_by_id("checkin_aeroplan_or_pnr").clear()
        self.driver.find_element_by_id("checkin_aeroplan_or_pnr").send_keys(Testvalues.data["%26$@"])
        self.driver.execute_script(
            Testvalues.fire_event_script + "fireEvent(document.getElementById('checkin_aeroplan_or_pnr'), 'input');")
        self.driver.execute_script(
            Testvalues.fire_event_script + "fireEvent(document.getElementById('checkin_aeroplan_or_pnr'), 'blur');")


        try:

            if self.driver.find_element_by_css_selector('input[id="checkin_aeroplan_or_pnr"][class~="ng-touched"]'):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def departure_city(self):

        # departure city field

        element = self.driver.find_element_by_id("checkin_location")

        if element:
            logging.info(self.site_name + " :departure city field exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: departure city element is not attached to the page document")

        self.driver.execute_script("document.getElementById('checkin_location').value='" + Testvalues.data["%27$@"] + "';")
        self.driver.execute_script(
            Testvalues.fire_event_script + "fireEvent(document.getElementById('checkin_location'), 'change');")
        self.driver.execute_script(
            Testvalues.fire_event_script + 'var predictionList = document.querySelectorAll(\'div[class="location-options"] ul[id="checkinLocationListOrginId"] li\');if (predictionList.length !== 0) {for (var i = 0; i < predictionList.length; i++) {if (predictionList[i].innerText.slice(0, 3).toLowerCase() === "' +
            Testvalues.data["%27$@"] + '".toLowerCase()) {predictionList[i].click();}}}')

        try:
            if self.data["%27$@"].lower() in self.driver.find_element_by_css_selector(
                    'span[data-ng-bind="cMagnetCheckIn.location.city.name"]').text.lower():
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form

        element = self.driver.find_element(By.ID, 'checin_submit_button')
        if element:
            element.click()
            logging.info(self.site_name + " :submit button exists")
        else:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        # except Exception:
        #     logging.error(
        #         self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")

        try:

            #  for error Message
            element = self.driver.find_element(By.ID, 'checin_submit_button')

            if element and "find your reservation" in element.text:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Desktop Site Tests Finished!!")
