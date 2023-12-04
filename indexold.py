import unittest

import logging
import datetime
import  glob


logging.basicConfig(filename="logs/%s.log"%(datetime.datetime.now().strftime("%m-%d-%Y")),
                    filemode="w", level=logging.INFO,
                    format="%(levelname)s: %(message)s (Time: %(asctime)s)")
test_file_strings = glob.glob('UnitTestcase*.py')
module_strings = [str[0:len(str)-3] for str in test_file_strings]

if __name__ == "__main__":
     unittest.main()

# #  get all tests from SearchText and HomePageTest class
# #  Aeroflot
# aerofloat = unittest.TestLoader().loadTestsFromTestCase(Aerofloat)
# # Aerlingus
# aerlingus = unittest.TestLoader().loadTestsFromTestCase(Aerlingus)
# #  Aeromexico
# aeromexico = unittest.TestLoader().loadTestsFromTestCase(Aeromexico)
# #  Airbaltic
# airbaltic = unittest.TestLoader().loadTestsFromTestCase(Airbaltic)
# #  Airchina
# airchina = unittest.TestLoader().loadTestsFromTestCase(Airchina)
# #  Aircanada
# aircanada = unittest.TestLoader().loadTestsFromTestCase(Aircanada)
# #  aireuropa
# aireuropa = unittest.TestLoader().loadTestsFromTestCase(Aireuropa)
# #  airfrance
# airfrance = unittest.TestLoader().loadTestsFromTestCase(Airfrance)
# #  alaskaairlines
# alaskaairlines = unittest.TestLoader().loadTestsFromTestCase(Alaskaairlines)
# #  alitaliaairlines
# alitaliaairlines = unittest.TestLoader().loadTestsFromTestCase(Alitaliaairlines)
# #  allnipponairways
# allnipponairways = unittest.TestLoader().loadTestsFromTestCase(Allnipponairways)
# #  americanairlines
# americanairlines = unittest.TestLoader().loadTestsFromTestCase(Americanairlines)
# # austrianairlines
# austrianairlines = unittest.TestLoader().loadTestsFromTestCase(Austrianairlines)
# # Britishairways
# britishairways = unittest.TestLoader().loadTestsFromTestCase(Britishairways)
# # cathaypacific
# cathaypacific = unittest.TestLoader().loadTestsFromTestCase(Cathaypacific)
# # Chinaeastern
# chinaeastern = unittest.TestLoader().loadTestsFromTestCase(Chinaeastern)
# # Chinasouthern
# chinasouthern = unittest.TestLoader().loadTestsFromTestCase(Chinasouthern)
# # Delta
# delta = unittest.TestLoader().loadTestsFromTestCase(Delta)
# # Easyjet
# easyjet = unittest.TestLoader().loadTestsFromTestCase(Easyjet)
# # Emirates
# emirates = unittest.TestLoader().loadTestsFromTestCase(Emirates)
# # Etihadairways
# etihadairways = unittest.TestLoader().loadTestsFromTestCase(Etihadairways)
# # Eurowings
# eurowings = unittest.TestLoader().loadTestsFromTestCase(Eurowings)
# # Finnair
# finnair = unittest.TestLoader().loadTestsFromTestCase(Finnair)
# # Frontier
# frontier = unittest.TestLoader().loadTestsFromTestCase(Frontier)
# # Iberia
# iberia = unittest.TestLoader().loadTestsFromTestCase(Iberia)
# # Japairlines
# japanairlines = unittest.TestLoader().loadTestsFromTestCase(Japanairlines)
# #  Jetblue
# jetblue = unittest.TestLoader().loadTestsFromTestCase(Jetblue)
# #  Klm
# klm = unittest.TestLoader().loadTestsFromTestCase(Klm)
# # Koreanair
# koreanair = unittest.TestLoader().loadTestsFromTestCase(Koreanair)
# # Lotpolish
# lotpolish = unittest.TestLoader().loadTestsFromTestCase(Lotpolish)
# # Lufthansa
# lufthansa = unittest.TestLoader().loadTestsFromTestCase(Lufthansa)
# # Norwegian
# norwegian = unittest.TestLoader().loadTestsFromTestCase(Norwegian)
# # Qatarairways
# qatarairways = unittest.TestLoader().loadTestsFromTestCase(Qatarairways)
# # Ryanair
# ryanair = unittest.TestLoader().loadTestsFromTestCase(Ryanair)
# # Sas
# sas = unittest.TestLoader().loadTestsFromTestCase(Sas)
# # Singaporeairlines
# singaporeairlines = unittest.TestLoader().loadTestsFromTestCase(Singaporeairlines)
# # Southwest
# southwest = unittest.TestLoader().loadTestsFromTestCase(Southwest)
# # Spiritairlines
# spiritairlines = unittest.TestLoader().loadTestsFromTestCase(Spiritairlines)
# # TapPortugal
# tapPortugal = unittest.TestLoader().loadTestsFromTestCase(TapPortugal)
# # Turkishairlines
# turkishairlines = unittest.TestLoader().loadTestsFromTestCase(Turkishairlines)
# # United
# united = unittest.TestLoader().loadTestsFromTestCase(United)
# # Wowair
# wowair = unittest.TestLoader().loadTestsFromTestCase(Wowair)
#
#
# test_suite = unittest.TestSuite([aerofloat, aerlingus, aeromexico, airbaltic, airchina, aircanada, aireuropa, airfrance, alaskaairlines, alitaliaairlines, allnipponairways, americanairlines, austrianairlines, britishairways, cathaypacific, chinaeastern, chinasouthern, delta, easyjet, emirates, etihadairways, eurowings, finnair, frontier, iberia, lufthansa, norwegian, qatarairways, ryanair, sas, singaporeairlines, southwest, spiritairlines, tapPortugal, turkishairlines, united, wowair])
#
#
#
# unittest.TextTestRunner(verbosity=2).run(test_suite)
#
