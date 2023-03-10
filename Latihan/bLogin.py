import unittest
from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import Select
#from locator import elem
#from data import inputan
#import baseRegister

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_success_login(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com")
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("re12@email.com")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()

        response1 = driver.find_element(By.CLASS_NAME, "ico-logout").text
        self.assertIn("Log out", response1)

    def test_b_failed_login(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com")
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("re12@email.com")
        driver.find_element(By.ID, "Password").send_keys("12345")
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()

        respon = driver.find_element(By.CLASS_NAME, "message-error")


if __name__ == '__main__':
    unittest.main()