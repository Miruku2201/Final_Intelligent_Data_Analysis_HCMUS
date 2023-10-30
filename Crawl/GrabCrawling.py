from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

sys.path.append("SupportMethod")
from Jsonfile import update, create


desired_capabilities = {
    "platformName": "android",
    "deviceName": "R58MB5EYBQM",
    "appPackage": "com.grabtaxi.passenger",
    "appActivity": "com.grab.pax.newface.presentation.newface.NewFace"
}


# Generating the driver by appium.
driver = webdriver.Remote(
    "http://localhost:4723/wd/hub", desired_capabilities=desired_capabilities
)

## Waiting the android application to launch
driver.implicitly_wait(15)

## Sign in to the Grab app.
driver.find_element(
    "xpath",
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView[2]",
).click()

## Wait for launching authorities
driver.implicitly_wait(20)

## Accept the map authority
driver.find_element(
    "id", "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
).click()

## Wait
driver.implicitly_wait(20)

## Click the Grab bike button
driver.find_element(MobileBy.ACCESSIBILITY_ID, "Xe máy, double tap to select").click()

## Wait for advertising
driver.implicitly_wait(20)

## Dismiss the advertise
driver.find_element("id", "com.grabtaxi.passenger:id/tvLeftButton").click()

## Toggle "MySchool" destination button
driver.find_element(MobileBy.ACCESSIBILITY_ID, "Ride to HCMUS in saved places, double tap to select").click()

## Get "departure" text
departure_text = driver.find_element("id", "com.grabtaxi.passenger:id/poi_item_title").text
departure_address = driver.find_element("id", "com.grabtaxi.passenger:id/poi_item_distance").text

print(str(departure_text) + str(departure_address))
grab_data = {
    "departureText": departure_text,
    "departureAddress": departure_address,
    "destinationText": None,
    "destinationAddress": None,
}

path = "./Database/GrabPrice/GrabPrice.json"
create(path, "grabPrice")
update()

print("stop")
