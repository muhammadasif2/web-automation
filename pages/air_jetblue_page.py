from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time


class JetblueCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "jetblue"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def first_name(self):
        # for first name test
        try:

            element = self.driver.find_element(By.ID, "firstName")

            if element:
                logging.info(self.site_name + " :first name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
            self.driver.find_element(By.ID, "firstName").clear()
            time.sleep(1)
            self.driver.find_element(By.ID, "firstName").send_keys(Testvalues.data["%1$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: first name element is not attached to the page document")

    def last_name(self):
        # for last name test
        try:

            element = self.driver.find_element(By.ID, "lastName")

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, "lastName").clear()

            self.driver.find_element(By.ID, "lastName").send_keys(Testvalues.data["%3$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: last name element is not attached to the page document")

    def airport_code(self):
        # for airport code test
        try:

            element = self.driver.find_element(By.ID, "departureCity")

            if element:
                logging.info(self.site_name + " :airport code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: airport code element is not attached to the page document")

            self.driver.execute_script(
                Testvalues.fire_event_script + "var letter = 'las';var selectObj = document.getElementById('departureCity');var autocompleteArrow = document.querySelector('input[id=\"departureCity\"]+div[class=\"autocomplete_arrow\"]');var dropdown, tempCode, autocompleteArrow;if (selectObj && autocompleteArrow && letter) {autocompleteArrow.click();autocompleteArrow.click();setTimeout(function () {dropdown = document.querySelector('div[class~=\"ac_results\"] ul');if (dropdown) {for (var i = 0; i < dropdown.childNodes.length; i++) {tempCode = dropdown.children[i].innerText.split('(')[1];if (tempCode) {if (tempCode.slice(0, -1).toLowerCase() === letter.toLowerCase()) {dropdown.children[i].click();selectObj.style.background = '#f19c4f';autocompleteArrow.style.background = '#f19c4f';}}}}}, 100);}")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: airport code element is not attached to the page document")

    def confirmation_code(self):
        # for confirmation code test
        try:

            element = self.driver.find_element(By.ID, "recordLocator")

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.ID, "recordLocator").clear()

            self.driver.find_element(By.ID, "recordLocator").send_keys(Testvalues.data["%26$@"])
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")

    def submit_button(self):
        # submitting form

        try:
            element = self.driver.find_element(By.CSS_SELECTOR,
                                          'div[class~="guestID"] button[id="continueButton"][name="submitButton"]')
            if element:
                element.click()
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
            element =  self.driver.find_element(By.CSS_SELECTOR,'table[class="errorOrQuitTable"] td[class="message"]')

        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
        try:
            if element and "We could not find your reservation. Please try another form of identification or see a JetBlue crewmember at the airport for assistance." in element.text:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

            logging.info(self.site_name + " :Desktop Site Tests Finished!!")
        except Exception:
            logging.info(self.site_name + " :Desktop Site Tests Finished!!")


class JetbluecheckinMobilePaage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "jetblue"
        logging.info(self.site_name + "  :Mobile site Tests start")

    def first_name(self):
        # for first name test
        try:

            element = self.driver.find_element(By.CSS_SELECTOR,'form div[class~="mat-form-field-infix"] input[name="firstName"]')

            if element:
                logging.info(self.site_name + " :first name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: first name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR,
                                'form div[class~="mat-form-field-infix"] input[name="firstName"]').clear()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR,
                                'form div[class~="mat-form-field-infix"] input[name="firstName"]').send_keys(
                Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('form div[class~=\"mat-form-field-infix\"] input[name=\"firstName\"]'), 'input');")
            time.sleep(1)
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: first name element is not attached to the page document")

        # TODO: Need to add UI effects test here.
        try:

            if "ng-valid" in self.driver.find_element(By.CSS_SELECTOR,
                                                 'div[class="mat-input-infix mat-form-field-infix"] input[placeholder="First Name*"]').get_attribute(
                    "class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.info(self.site_name + " :Assertion mismatch after firing event on input field")

    def last_name(self):
        # for last name test
        try:

            element =  self.driver.find_element(By.CSS_SELECTOR,'form div[class~="mat-form-field-infix"] input[name="lastName"]')

            if element:
                logging.info(self.site_name + " :last name field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR,
                                'form div[class~="mat-form-field-infix"] input[name="lastName"]').clear()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR,
                                'form div[class~="mat-form-field-infix"] input[name="lastName"]').send_keys(
                Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('form div[class~=\"mat-form-field-infix\"] input[name=\"lastName\"]'), 'input');")

            # TODO: Need to add UI effects test here.

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def confirmation_code(self):
        # for confirmation code test

        try:
            element =  self.driver.find_element(By.CSS_SELECTOR,'form div[class~="mat-form-field-infix"] input[name="confirmationCode"]')

            if element:
                logging.info(self.site_name + " :confirmation code field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: confirmation code element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR,
                                'form div[class~="mat-form-field-infix"] input[name="confirmationCode"]').clear()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR,
                                'form div[class~="mat-form-field-infix"] input[name="confirmationCode"]').send_keys(
                Testvalues.data["%26$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.querySelector('form div[class~=\"mat-form-field-infix\"] input[name=\"confirmationCode\"]'), 'input');")
            time.sleep(1)

            # TODO: Need to add UI effects test here.

            if "ng-valid" in element.get_attribute("class"):
                logging.info(self.site_name + " :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + " :Assertion mismatch after firing event on input field")
        except Exception:
            logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

    def airport_code(self):
        # for airport code test

        try:

            element =  self.driver.find_element(By.CSS_SELECTOR,'form div[class~="mat-form-field-infix"] input[name="departureAirport"]')

            if element:
                logging.info(self.site_name + " :Departure City field exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: airport code element is not attached to the page document")
            self.driver.find_element(By.CSS_SELECTOR,'form div[class~=\"mat-form-field-infix\"] input[name=\"departureAirport\"]').clear()

            self.driver.execute_script(
                Testvalues.fire_event_script + "function fireEvent(element, event) {if (document.createEventObject) {var evt = document.createEventObject();return element.fireEvent('on'+event, evt);} else {var evt = document.createEvent('HTMLEvents');evt.initEvent(event, true, true);return !element.dispatchEvent(evt);}} var letter = 'las';var selectObj = document.querySelector('form div[class~=\"mat-form-field-infix\"] input[name=\"departureAirport\"]');if (selectObj && letter) {selectObj.value = letter;fireEvent(selectObj, 'click');fireEvent(selectObj, 'input');setTimeout(function () {var tempCode;var mtAutocompleteList = document.querySelectorAll('div[class~=\"mt-autocomplete\"] div[class~=\"mat-autocomplete-panel\"] mat-option');if (mtAutocompleteList) {for (var i = 0; i < mtAutocompleteList.length; i++) {mtAutocompleteList[i].click();}}}, 100);}")
            time.sleep(3)
        except Exception:
            logging.error(
                self.site_name + " :Message: stale element reference: airport code element is not attached to the page document")

    def submit_button(self):
        # submitting form
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, 'button[class~="jb-btn-primary"]')
            element.click()
            if element:
                element.click()
                self.driver.execute_script(Testvalues.fire_event_script + "document.querySelector('button[class~=\"jb-btn-primary\"]').click();")
                logging.info(self.site_name + " :submit button exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: submit button element is not attached to the page document")
            element = WebDriverWait(
                self.driver,
                10

            ).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p[class="ng-star-inserted"]')))
            print(element.text)
            if element and "could not find your reservation" in element.text:
                logging.info(self.site_name + " :error message exists")
            else:
                logging.info(
                    self.site_name + " :Message: stale element reference: error message element is not attached to the page document")
        except Exception:
            logging.info(
                self.site_name + " :Message: stale element reference: error message element is not attached to the page document")

        logging.info(self.site_name + " :Mobile Site Tests Finished!!")
