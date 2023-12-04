from selenium import webdriver


class Checkinemulation():

    def __init__(self):
        mobile_emulation = {
            # "deviceName": "Apple iPhone 3GS"
            # "deviceName": "Apple iPhone 4"
            #   "deviceName": "Nexus 10"
            "deviceName": "iPhone 6/7/8"
            # "deviceName": "Apple iPhone 6 Plus"
            # "deviceName": "BlackBerry Z10"
            # "deviceName": "BlackBerry Z30"
            # "deviceName": "Google Nexus 4"
            # "deviceName": "Google Nexus 5"
            # "deviceName": "Google Nexus S"
            # "deviceName": "HTC Evo, Touch HD, Desire HD, Desire"
            # "deviceName": "HTC One X, EVO LTE"
            # "deviceName": "HTC Sensation, Evo 3D"
            # "deviceName": "LG Optimus 2X, Optimus 3D, Optimus Black"
            # "deviceName": "LG Optimus G"
            # "deviceName": "LG Optimus LTE, Optimus 4X HD"
            # "deviceName": "LG Optimus One"
            # "deviceName": "Motorola Defy, Droid, Droid X, Milestone"
            # "deviceName": "Motorola Droid 3, Droid 4, Droid Razr, Atrix 4G, Atrix 2"
            # "deviceName": "Motorola Droid Razr HD"
            # "deviceName": "Nokia C5, C6, C7, N97, N8, X7"
            # "deviceName": "Nokia Lumia 7X0, Lumia 8XX, Lumia 900, N800, N810, N900"
            # "deviceName": "Samsung Galaxy Note 3"
            # "deviceName": "Samsung Galaxy Note II"
            # "deviceName": "Samsung Galaxy Note"
            # "deviceName": "Samsung Galaxy S III, Galaxy Nexus"
            # "deviceName": "Samsung Galaxy S, S II, W"
            # "deviceName": "Samsung Galaxy S4"
            # "deviceName": "Sony Xperia S, Ion"
            # "deviceName": "Sony Xperia Sola, U"
            # "deviceName": "Sony Xperia Z, Z1"
            # "deviceName": "Amazon Kindle Fire HDX 7″"
            # "deviceName": "Amazon Kindle Fire HDX 8.9″"
            # "deviceName": "Amazon Kindle Fire (First Generation)"
            # "deviceName": "Apple iPad 3 / 4"
            # "deviceName": "BlackBerry PlayBook"
            # "deviceName": "Google Nexus 10"
            # "deviceName": "Google Nexus 7 2"
            # "deviceName": "Google Nexus 7"
            # "deviceName": "Motorola Xoom, Xyboard"
            # "deviceName": "Samsung Galaxy Tab 7.7, 8.9, 10.1"
            # "deviceName": "Samsung Galaxy Tab"
            # "deviceName": "Notebook with touch"

            # Or specify a specific build using the following two arguments
            # "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
            # "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
        }

        # Define a variable to hold all the configurations we want
        chrome_options = webdriver.ChromeOptions()

        # Add the mobile emulation to the chrome options variable
        chrome_emulation = chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        # Create driver, pass it the path to the chromedriver file and the special configurations you want to run

        abc = webdriver.Chrome(
            executable_path='/home/asif/Downloads/chromedriver',
            options=chrome_options)



