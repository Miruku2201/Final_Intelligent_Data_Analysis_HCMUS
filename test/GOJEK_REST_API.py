from appium import webdriver

desired_capabilities = {
    "platformName": "android",
    "deviceName": "R58MB5EYBQM",
    "appPackage": "com.grabtaxi.passenger",
    "appActivity": "com.grab.pax.newface.presentation.newface.NewFace",
}

driver = webdriver.Remote(
    "http://localhost:4723/wd/hub", desired_capabilities=desired_capabilities
)

driver.implicitly_wait(15)

driver.find_element(
    "xpath",
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView[2]",
).click()
