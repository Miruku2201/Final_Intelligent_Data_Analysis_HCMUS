from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import json
import sys

sys.path.append("SupportMethod")
from Jsonfile import update, create


class GrabCrawler:
    with open("./assets/GRAB.json", "r") as fread:
        grab_params = json.loads(fread.read())
        desired_capabilities = grab_params["desired_capabilities"]
        location_id = grab_params["Locations_id"]
        location_address = grab_params["Locations_address"]

    def __init__(self):
        # Generating the driver by appium.
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4723/wd/hub",
            desired_capabilities=GrabCrawler.desired_capabilities,
        )

    def go_to(self, destination: str):
        ## Waiting the android application to launch
        self.driver.implicitly_wait(15)

        ## Sign in to the Grab app.
        self.driver.find_element(
            "xpath",
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView[2]",
        ).click()

        #############################################################
        ## Wait for launching authorities
        self.driver.implicitly_wait(20)

        self.driver.find_element(
            "xpath",
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView",
        ).click()
        self.driver.implicitly_wait(20)

        # self.driver.find_element(
        #     "xpath",
        #     '//android.widget.LinearLayout[@content-desc="0329 601 106"]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView',
        # ).click()
        #################################################################
        self.driver.implicitly_wait(20)

        # self.driver.find_element(
        #     "id", "com.grabtaxi.passenger:id/gds_button_text"
        # ).click()
        self.driver.implicitly_wait(20)

        ## Accept the map authority
        self.driver.find_element(
            "id",
            "com.android.permissioncontroller:id/permission_allow_foreground_only_button",
        ).click()

        ## Wait
        self.driver.implicitly_wait(20)

        ## Click the Grab bike button
        self.driver.find_element(
            MobileBy.ACCESSIBILITY_ID, "Xe máy, double tap to select"
        ).click()

        ## Wait for advertising
        self.driver.implicitly_wait(20)

        ## Dismiss the advertise
        try:
            self.driver.find_element(
                "id", "com.grabtaxi.passenger:id/tvLeftButton"
            ).click()
        except:
            pass

        ## Toggle "MySchool" destination button
        self.driver.find_element(
            MobileBy.ACCESSIBILITY_ID, GrabCrawler.location_id[destination]
        ).click()

        ## Get "departure" text
        departure_text = self.driver.find_element(
            "id", "com.grabtaxi.passenger:id/bottom_wheel_item_info_title"
        ).text
        # departure_address = self.driver.find_element(
        #     MobileBy.ACCESSIBILITY_ID, "com.grabtaxi.passenger:id/bottom_wheel_item_info_detail"
        # ).text

        print("OKE")
        # self.driver.find_element(AppiumBy.ID, "com.grabtaxi.passenger:id/btn_confirm").click()
        # self.driver.find_element(
        #     "xpath",
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[6]/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.TextView",
        # ).click()

        ## Get the price and type of Grab
        self.driver.implicitly_wait(20)
        time.sleep(10)
        action = TouchAction(self.driver)
        action.long_press(None, 326, 1520).move_to(None, 729, 956).release().perform()

        self.driver.implicitly_wait(20)
        types = self.driver.find_elements(
            AppiumBy.ID, "com.grabtaxi.passenger:id/xsell_confirmation_taxi_type_name"
        )
        prices = self.driver.find_elements(
            AppiumBy.ID, "com.grabtaxi.passenger:id/fareTextView"
        )

        ##############################################################################################################################/
        byVehicle = []
        for __type, __price in zip(types, prices):
            byVehicle.append({"type": __type.text, "price": __price.text})

        print(byVehicle)

        grab_data = {
            "departureText": departure_text,
            # "departureAddress": departure_address,
            "departureAddress": GrabCrawler.location_address[departure_text],
            "destinationText": destination,
            "destinationAddress": GrabCrawler.location_address[destination],
            "byVehicle": byVehicle,
        }
        path = "./Database/GrabPrice/GrabPrice.json"
        create(path, "grabPrice")
        update(grab_data, "grabPrice", path)
        return grab_data
