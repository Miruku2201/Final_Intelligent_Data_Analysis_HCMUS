from appium import webdriver

desired_capabilities  = {
  "platformName": "android",
  "deviceName": "R58MB5EYBQM",
  "appPackage": "com.grabtaxi.passenger",
  "appActivity": "com.grab.pax.newface.presentation.newface.NewFace"
}


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities= desired_capabilities)
