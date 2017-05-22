import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:/Users/obg/Downloads/chromedriver.exe")
driver.maximize_window()
driver.get("http://order.adfenix.com/#/lansfast/?id=4ask4hk5ab2jksv6&token=kocLK8xBrk6PHJU9hUBD8Q")

primary_logo_locator = "//div[contains(@class, 'logo bg-primary logo-section')]"

logout_locator = '//span[contains(@class, "sign-out text-uppercase ng-scope")]'
print("====================================")
print("Logging into system")
print("====================================")

print("Verify whether Logo is present or not")
try:
    _logo = driver.find_element(By.XPATH, primary_logo_locator).is_displayed()
except Exception as err:
    print(err)
assert _logo is True, "Failed"
print('Pass. Yes, logo is present')

print("Verify whether Logout option is present or not")
time.sleep(10)

try:
    _logout = driver.find_element(By.XPATH, logout_locator).is_displayed()
except Exception as err:
    print(err)
assert _logout is True, "Logout option not loaded yet"
print('Pass. Yes, logout is present')

time.sleep(10)
logout_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logout_locator))

driver.implicitly_wait(10)
logout_element.click()
time.sleep(10)

print("====================================")
print("Successfully logout from the system")
print("====================================")
driver.quit()