from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class logintest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/obg/Downloads/chromedriver.exe")
        self.driver.get("htpps://www.facebook.com/")
    def test_login(self):
        driver = self.driver
        facebookUsername= ""
        facebookPassword = ""
        emailfieldID = "email"
        passfieldID = "pass"
        logiButtonXpath = "//input[@value='Log In']"
        fbLogoXpath = "(//a[contains(@href, 'logo')])[1]"

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailfieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passfieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logiButtonXpath))


        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
