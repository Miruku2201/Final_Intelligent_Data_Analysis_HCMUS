from appium import webdriver

desired_capabilities = {
    "platformName": "android",
    "deviceName": "R58MB5EYBQM",
    "appPackage": "com.grabtaxi.passenger",
    "appActivity": "com.grab.pax.newface.presentation.newface.NewFace",
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

driver.find_element("id", "com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
print("stop")

