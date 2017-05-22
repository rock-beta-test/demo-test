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


try:
    _logo = driver.find_element(By.XPATH, primary_logo_locator).is_displayed()
except Exception as err:
    print(err)
assert _logo is True, "Failed"

print(" Navigate to listing page")
primary_logo_locatorElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(primary_logo_locator))
time.sleep(10)
primary_logo_locatorElement.click()

# //span[text()= "Search"]
search_btn_locator = '//button[contains(@class, "btn-search")]'
search_input_box_locator = '//input[contains(@placeholder, "keywords...")]'
matched_keyword_locator = '//div[contains(text(), "Norra Villagatan 18 - Slottsbron")]'
not_matched_loator = '//div[contains(@class, "search-error clearfix")]'

time.sleep(2)
search_btn_locatorElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(search_btn_locator))
time.sleep(2)
search_input_box_locatorElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(search_input_box_locator))


# matched_keyword_locatorElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(matched_keyword_locator))
#
# time.sleep(2)
# not_matched_loatorElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(not_matched_loator))



print(" - > Search with exact match Keyword")
search_input_box_locatorElement.clear()
search_input_box_locatorElement.send_keys("Norra Villagatan 18 - Slottsbron")
time.sleep(2)
search_btn_locatorElement.click()
time.sleep(2)

try:
    is_matched = driver.find_element(By.XPATH, matched_keyword_locator).is_displayed()
except Exception as err:
    print(err)
assert is_matched is True, " X -> Failed.  Result not found with exact match."
print(" - > Pass. Result found with exact match")

print(" - > Search with partial match Keyword")
search_input_box_locatorElement.clear()
search_input_box_locatorElement.send_keys("Villagatan 18")
time.sleep(2)
search_btn_locatorElement.click()
time.sleep(2)

try:
    is_matched = driver.find_element(By.XPATH, matched_keyword_locator).is_displayed()
except Exception as err:
    print(err)
assert is_matched is True, " X -> Failed.  Result not found with partial match"
print(" - > Pass. Result found with partial match")

print(" - > Search with unknown Keyword")
search_input_box_locatorElement.clear()
search_input_box_locatorElement.send_keys("testing")
time.sleep(2)
search_btn_locatorElement.click()
time.sleep(2)

try:
    is_matched = driver.find_element(By.XPATH, not_matched_loator).is_displayed()
except Exception as err:
    print(err)
assert is_matched is True, " X -> Failed.  Result found with unknown keyword"

print(" - > Pass. No result found")

print("====================================")
print("Logging out from the system")
time.sleep(10)
try:
    _logout = driver.find_element(By.XPATH, logout_locator).is_displayed()
except Exception as err:
    print(err)

assert _logout is True, "logout option not loaded yet"

time.sleep(10)
logout_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logout_locator))

driver.implicitly_wait(10)
logout_element.click()
time.sleep(10)


print("Successfully logout from the system")
print("====================================")
driver.quit()