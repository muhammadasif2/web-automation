from testvalues import Testvalues
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class AeroflotCheckinDesktopPage():

    def __init__(self, driver):
        self.driver = driver
        self.site_name = "Aeroflot"
        logging.info(self.site_name + "  :Desktop site Tests start")

    def first_name(self):
        element = WebDriverWait(
            self.driver,
            100

        ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#pnr')))

        if element:
            logging.info(self.site_name + "  :confirmation code field exists")
        else:
            logging.info(
                self.site_name + "  :Message: stale element reference: confirmation code element is not attached to the page document")
        self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('pnr'), 'DOMFocusIn');")
        element.clear()
        element.send_keys(Testvalues.data["%26$@"])
        self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementById('pnr'), 'DOMFocusOut');")

        # except Exception:
        #     logging.error(
        #         self.site_name + "  :Message: stale element reference: confirmation code element is not attached to the page document")

        print(self.data["%26$@"].upper())
        print(self.driver.find_element_by_id("pnr").get_attribute("value"))
        if self.data["%26$@"].upper() in self.driver.find_element_by_id("pnr").get_attribute("value"):

            logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
        else:
            logging.info(self.site_name + "  :Assertion mismatch after firing event on input field")
        # except Exception:
        #     logging.error(self.site_name + "  :Assertion mismatch after firing event on input field")

    def last_name(self):
        # for last name test
        try:
            self.driver.find_element(By.ID, "last-name")

            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('last-name'), 'DOMFocusIn');")
            if self.driver.find_element(By.ID, "last-name"):
                logging.info(self.site_name + "  :last name field exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: last name element is not attached to the page document")
            self.driver.find_element(By.ID, "last-name").clear()

            self.driver.find_element(By.ID, "last-name").send_keys(Testvalues.data["%3$@"])
            self.driver.execute_script(
                Testvalues.fire_event_script + "fireEvent(document.getElementById('last-name'), 'DOMFocusOut');")

        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: last name element is not attached to the page document")


            if Testvalues.data["%3$@"].upper() in self.driver.find_element(By.ID, "last-name").get_attribute("value"):
                logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
            else:
                logging.info(self.site_name + "  :Assertion mismatch after firing event on input field")
        # except Exception:
        #     logging.error(self.site_name + "  :Assertion mismatch after firing event on input field")

    def submit_button(self):
        # submitting form and checking on the error message
        try:

            element = self.driver.find_element(By.CSS_SELECTOR, '#btn-search')
            if element:
                element.click()
                logging.info(self.site_name + "  :submit button exists")
            else:
                logging.info(
                    self.site_name + "  :Message: stale element reference: submit button element is not attached to the page document")
        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: submit button element is not attached to the page document")
        try:

            element = WebDriverWait(
                self.driver,
                20

            ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[class~="alert-message"]')))
            if element:
                logging.info(self.site_name + "  :error message exists")
        except Exception:
            logging.error(
                self.site_name + "  :Message: stale element reference: error message element is not attached to the page document")
        logging.info(self.site_name + "  :Desktop Site Tests Finished!!")


# class AeroflotCheckinMobilePage():

#     def __init__(self, driver):
#         self.driver = driver
#         self.site_name = "Aeroflot"
#         logging.info(self.site_name + "  :Mobile site Tests starts")

#     def confirmation_code(self):
#         # for confirmation code test
#         try:

#             element = WebDriverWait(
#                 self.driver,
#                 30

#             ).until(EC.presence_of_element_located((By.NAME, 'pnrFf')))

#             if element:
#                 logging.info(self.site_name + " :confirmation code field exists")
#             else:
#                 logging.error(
#                     "Message: stale element reference: confirmation code element is not attached to the page document")
#             self.driver.execute_script(
#                 Testvalues.fire_event_script + "fireEvent(document.getElementsByName('pnrFf')[0], 'focus');")

#             if "is-focused" in element.find_element_by_xpath("..").get_attribute("class"):
#                 logging.info(self.site_name + ":Testing UI effects of firing event on input field")
#             else:
#                 logging.error(self.site_name + " :Assertion mismatch after firing event on input field")
#             self.driver.find_element_by_name("pnrFf").clear()
#             self.driver.find_element_by_name("pnrFf").send_keys(Testvalues.data["%26$@"])
#             self.driver.execute_script(Testvalues.fire_event_script + "fireEvent(document.getElementsByName('pnrFf')[0], 'blur');")
#         except Exception:
#             logging.error(self.site_name + " :Assertion mismatch after firing event on input field")

#     def last_name(self):
#         # for last name test

#         try:
#             element = self.driver.find_element_by_name("lastName")

#             if self.driver.find_element_by_name("lastName"):
#                 logging.info(self.site_name + "  :last name field exists")
#             else:
#                 logging.info(
#                     self.site_name + "  :Message: stale element reference: last name element is not attached to the page document")
#             self.driver.execute_script(
#                 Testvalues.fire_event_script + "fireEvent(document.getElementsByName('lastName')[0], 'focus');")

#             if "is-focused" in element.find_element_by_xpath("..").get_attribute("class"):
#                 logging.info(self.site_name + "  :Testing UI effects of firing event on input field")
#             else:
#                 logging.info(self.site_name + "  :Assertion mismatch after firing event on input field")
#             self.driver.find_element_by_name("lastName").clear()

#             self.driver.find_element_by_name("lastName").send_keys(Testvalues.data["%3$@"])
#             self.driver.execute_script(
#                 Testvalues.fire_event_script + "fireEvent(document.getElementsByName('lastName')[0], 'blur');")
#         except Exception:
#             logging.info(
#                     self.site_name + "  :Message: stale element reference: last name element is not attached to the page document")
#     def submit_button(self):
#         # submitting form
#         try:
#             element = WebDriverWait(
#                 self.driver,
#                 10

#             ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="sbmt-checkin-0"] button[id="sbmt-checkin-0-continue"]')))

#             if element:
#                 element.click()

#                 logging.info(self.site_name + "  :submit button exists")
#             else:
#                 logging.info(
#                     self.site_name + "  :Message: stale element reference: submit button element is not attached to the page document")
#         except Exception:
#             logging.info(
#                     self.site_name + "  :Message: stale element reference: submit button element is not attached to the page document")
#         try:

#             element = WebDriverWait(
#                 self.driver,
#                 10

#             ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[data-aria-translate="flow.message.unableToLocatePnr.message"]')))

#             if element:
#                 logging.info(self.site_name + "  :error message exists")
#             else:
#                 logging.info(
#                     self.site_name + "  :Message: stale element reference: error message element is not attached to the page document")
#             try:
#                 WebDriverWait(
#                     self.driver,
#                     10

#                 ).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-title"]')))
#         except Exception:
#             logging.info(
#                 self.site_name + "  :Message: stale element reference: error message element is not attached to the page document")

#         logging.info(self.site_name + "  :Mobile Site Tests Finished!!")
