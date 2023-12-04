import unittest
import os

from tests.test_aeroflot_checkin import Aeroflot
from tests.test_aerlingus_checkin import Aerolingus
from tests.test_aeromexico_checkin import Aeromexico
from tests.test_airbaltic_checkin import Airbaltic
from tests.test_airchina_checkin import Airchina
from tests.test_aireuropa_checkin import Aireuropa

from tests.test_airfrance_checkin import Airfrance
from tests.test_alaskaairlines_checkin import Alaskaair
from tests.test_alitaliaairlines_checkin import Airalitalia
from tests.test_allnipponair_checkin import Allnipponair
from tests.test_americanairlines_checkin import AmericanArilines
from tests.test_austrianairlines_checkin import AustrianAir
from tests.test_britishairways_checkin import British
from tests.test_brusselairlines_checkin import Brusselairlines
from tests.test_cathaypacific_checkin import Catheypacific
from tests.test_chinaeaster_checkin import Chinaeastern
from tests.test_chinasouthern_checkin import Chinasouthern
from tests.test_delta_checkin import Delta
from tests.test_easyjet_checkin import Easyjet
from tests.test_emirate_checkins import Emirates
from tests.test_etihadairways_checkin import Etihadairways
from tests.test_eurowings_checkin import Eurowing
from tests.test_finnair_checkin import Finnair
from tests.test_frontier_checkin import Frontier
from tests.test_iberia_checkin import Iberia
from tests.test_japanairlines_checkin import Japanairlines
from tests.test_jetblue_checkin import Jetblue
from tests.test_klm_checkin import Klm
from tests.test_koreanair_checkin import Koreanair
from tests.test_lotpolish_checkin import Lotpolish
from tests.test_lufthansa_checkin import Lufthansa
from tests.test_norwegian_checkin import Norwegian
from tests.test_qatarair_checkin import Qatarair
from tests.test_ryanair_checkin import Ryanair
from tests.test_sas_checkin import Sas
from tests.test_singapurair_checkin import Singapurair
from tests.test_southwest_checkin import Southwest
from tests.test_spiritairliens_checkin import Spiritair
from tests.test_tapPortugal_checkin import Tapportugal
from tests.test_turkishairlines_checkin import Turkishairlines
from tests.test_united_checkin import Unitedairlines
from tests.test_wowair_checkin import Wowair
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
import datetime
import os
from selenium.webdriver.remote.webelement import WebElement
from  pathlib import Path
from  logfilecode import Logfile
import HtmlTestRunner
from os.path import dirname, realpath


class CompleteUnitTest():

    filepath = realpath(__file__)
    basepath = dirname(filepath)

    def __init__(self):

        Logfile.create_log_file(self)

        if __name__ == "__main__":
          unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/asif/PycharmProjects/Properseleniumtests/reports'))
        Logfile.create_log_file(self)

CompleteUnitTest()