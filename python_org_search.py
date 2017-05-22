from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#
#
# driver = webdriver.Chrome("C:/Users/obg/Downloads/chromedriver.exe")
# driver.maximize_window()
# driver.get("http://quality-leads-endurance.blogspot.com/")
#
# WebDriverWait(driver, 10).until(lambda driver: driver.title)
#
# print("--------------------------")
# print("Verified the browser title")
# if "Quality is the secret of endurance" == driver.title:
#     print("page title is matched")
# else:
#     print("page title is Not matched yet")
#
#
# print("--------------------------")
# print("Checking whether Linkedin button link is there or not")
# linkedin_btn_locator = '//a[contains(@href, "http://www.linkedin.com/in/obaidulgaffer")]'
# linkedinButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(linkedin_btn_locator))
#
# try:
#     linkedin_button = driver.find_element(By.XPATH, linkedin_btn_locator).is_displayed()
# except Exception as err:
#     print(err)
# assert linkedin_button is True, "not present"
# print('yes, linkedin button link is present')
#
#
# print("--------------------------")
# print("Verify whether blog post title is present and clickable or not")
# post_link_locator = '//a[contains(@href, "http://quality-leads-endurance.blogspot.com/2014/10/software-agility-scaling-depends-upon.html") and (text() = "Software agility scaling depends upon appropriate Use Cases indeed.")]'
#
# try:
#     is_present_post_link_locator = driver.find_element_by_link_text("Software agility scaling depends upon appropriate Use Cases indeed.").is_displayed()
# except Exception as err:
#     print(err)
# assert is_present_post_link_locator is True, "Not present"
# print('yes, link is present')
# post_link_locatorElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(post_link_locator))
# print(post_link_locatorElement)
# post_link_locatorElement.click()
#
# # driver.find_element(By.XPATH,linkedin_btn_locator).is_displayed()
# # linkedinButtonElement.click()
# # WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(linkedin_btn_locator))
#
# driver.quit()



# driver = webdriver.Chrome("C:/Users/obg/Downloads/chromedriver.exe")
# driver.get("http://www.facebook.com/")
# print("Going to login to the FB")
#
# facebookUsername= "i.am.stunning.intellect@gmail.com"
# facebookPassword = "e0.123456789"
# emailfieldID = "email"
# passfieldID = "pass"
# logiButtonXpath = "//input[@value='Log In']"
# fbLogoXpath = "(//a[contains(@href, 'logo')])[1]"
#
# emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailfieldID))
# passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passfieldID))
# loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logiButtonXpath))
#
# # emailFieldElement = driver.find_element(By.ID, emailfieldID)
# # passFieldElement = driver.find_element(By.ID, passfieldID)
# # loginButtonElement1 = driver.find_element(By.XPATH, logiButtonXpath)
#
# emailFieldElement.clear()
# emailFieldElement.send_keys(facebookUsername)
# passFieldElement.clear()
# passFieldElement.send_keys(facebookPassword)
#
#
# loginButtonElement.click()
# WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))
#
# driver.close()


# --------------------#


from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/Users/obg/Downloads/chromedriver.exe")
driver.maximize_window()

driver.get("http://order.adfenix.com/#/lansfast/?id=4ask4hk5ab2jksv6&token=kocLK8xBrk6PHJU9hUBD8Q")
# seconds

primary_logo_locator = "//div[contains(@class, 'logo bg-primary logo-section')]"
try:
    _logo = driver.find_element(By.XPATH, primary_logo_locator).is_displayed()
except Exception as err:
    print(err)
assert _logo is True, "Failed"
print('yes, logo is present')
primary_logo_locatorElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(primary_logo_locator))
time.sleep(10)
print("primary_logo_locatorElement:", primary_logo_locatorElement)
primary_logo_locatorElement.click()
# driver.find_element(By.XPATH, primary_logo_locatorElement).click()

logout_locator2 = '//span[contains(@class, "sign-out text-uppercase ng-scope")]'

print("logout_locator", logout_locator2)

time.sleep(10)
try:
    _logout = driver.find_element(By.XPATH, logout_locator2).is_displayed()
    # logout_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logout_locator2))
except Exception as err:
    print(err)

assert _logout is True, "logout option not loaded yet"
print('yes, logout is present')

time.sleep(10)
logout_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logout_locator2))

driver.implicitly_wait(10)
# logout_element = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(logout_locator2))
print("this is logout element", logout_element)
logout_element.click()
time.sleep(10)






# youtube_locator = '//button[contains(@aria-label, "Watch Presenting Home Booster by Adfenix")]'
# youtube_btn = driver.find_element(By.XPATH, youtube_locator).is_displayed()
#
# if youtube_btn == True:
#     driver.find_element(By.XPATH, youtube_btn).click()
# else:
#     print("Item is not loaded")
#
# driver.find_element(By.XPATH, logout_locator2).click()

# list_navigate_locator = "//span[contains(text(), 'Mina Listningar')]"
# logout_locatorElement = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(logout_locator2))
# if driver.find_element_by_xpath(logout_locator2).is_displayed()== True:
#     WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(primary_logo_locator))
#     driver.implicitly_wait(10)
#     driver.find_element(By.XPATH, logout_locator2).click()
# else:
#     print("logout is not loaded")
#
# mina_listningar_header = "//h2[contains(text(), 'Mina listningar')]"
#
# try:
#     page_header = driver.find_element(By.XPATH, mina_listningar_header).is_displayed()
# except Exception as err:
#     print(err)
#
# assert page_header is True, "Failed"
# print ("yes, header is present")

driver.quit()














logout_locator = (By.XPATH,"//span[contains(text(), 'Logga ut')]")

# assert primary_logo_locator is True,
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source



# driver.find_element(By.XPATH, submit).click()

# elem = driver.find_element_by_xpath("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
