import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:/Users/obg/Downloads/chromedriver.exe")
driver.maximize_window()

driver.get("http://order.adfenix.com/#/lansfast/?id=4ask4hk5ab2jksv6&token=kocLK8xBrk6PHJU9hUBD8Q")

primary_logo_locator = "//div[contains(@class, 'logo bg-primary logo-section')]"
logout_locator = '//span[contains(@class, "sign-out text-uppercase ng-scope")]'
Redigera_btn_locator = '//a[contains(@data-ng-click, "facebookAd.toggleMode()")]/span[contains(text(), "Redigera annons")]'
Förhandsgranska_btn_locator = '//a[contains(@data-ng-click, "facebookAd.toggleMode()")]/span[contains(text(), "Förhandsgranska annons")]'
modal_open_btn_locator = '//button[contains(@data-translate, "ORDER_CHANGE_IMAGE_TEXT")]'
modal_title_locator = '//h4[contains(@data-translate, "MEDIA_LIBRARY_MODAL_TITLE")]'
modal_cancel_locator = '//button[contains(@data-translate, "MEDIA_LIBRARY_MODAL_CANCEL_BUTTON_TEXT")]'


print("************************************")
print("Logging into system")
print("************************************")

time.sleep(2)
try:
    _logo = driver.find_element(By.XPATH, primary_logo_locator).is_displayed()
except Exception as err:
    print(err)
assert _logo is True, "Failed"

time.sleep(2)
Redigera_btn_locator_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(Redigera_btn_locator))



Redigera_btn_locator_element.click()
time.sleep(2)


try:
    modal_open_btn = driver.find_element(By.XPATH, modal_open_btn_locator).is_displayed()
except Exception as err:
    print(err)

assert modal_open_btn is True, "x Fail. Modal is not opened yet"
print("Pass. Modal has been opened successfully")
time.sleep(2)
modal_open_btn_locator_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(modal_open_btn_locator))
print("modal_open_btn_locator_element", modal_open_btn_locator_element)
modal_open_btn_locator_element.click()
time.sleep(5)

try:
    is_modal_open = driver.find_element(By.XPATH, modal_title_locator).is_displayed()
except Exception as err:
    print(err)

assert is_modal_open is True, "x Fail. Modal is not opened yet"
print("Pass. Modal has been opened successfully")
time.sleep(5)

print("Now closing the modal")
modal_cancel_locator_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(modal_cancel_locator))
time.sleep(5)

try:
    is_modal_open = driver.find_element(By.XPATH, modal_cancel_locator).is_displayed()
except Exception as err:
    print(err)

assert is_modal_open is True, "Modal is not closed yet"
modal_cancel_locator_element.click()
print("Pass. Modal has been closed successfully")


time.sleep(10)
try:
    _logout = driver.find_element(By.XPATH, logout_locator).is_displayed()
except Exception as err:
    print(err)

assert _logout is True, "Logout option not loaded yet"

time.sleep(10)
logout_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logout_locator))

driver.implicitly_wait(10)
logout_element.click()
time.sleep(3)
driver.save_screenshot("Modal_has_been_closed.png")
time.sleep(2)
print("************************************")
print("Logging out from the system")
print("Successfully logout from the system")
print("*************************************")
driver.quit()