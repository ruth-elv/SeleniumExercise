import unittest
from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
#from locator import elem
#from data import inputan
#import baseRegister

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_success_checkout(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com")
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("re12@email.com")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()

        response1 = driver.find_element(By.CLASS_NAME, "ico-logout").text
        self.assertIn("Log out", response1)
        
        driver.find_element(By.LINK_TEXT, "$25 Virtual Gift Card").click();
        driver.find_element(By.ID, "giftcard_2_RecipientName").send_keys("Ruth")
        driver.find_element(By.ID, "giftcard_2_RecipientEmail").send_keys("re12@email.com")
        driver.find_element(By.ID, "add-to-cart-button-2").click()

        respon = driver.find_element(By.ID, "bar-notification")

    def test_b_failed_checkout(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com")
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "ico-login").click()
        driver.find_element(By.ID, "Email").send_keys("re12@email.com")
        driver.find_element(By.ID, "Password").send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, ".button-1.login-button").click()

        response1 = driver.find_element(By.CLASS_NAME, "ico-logout").text
        self.assertIn("Log out", response1)
        
        driver.find_element(By.LINK_TEXT, "$25 Virtual Gift Card").click();
        driver.find_element(By.ID, "add-to-cart-button-2").click()

        respon1 = driver.find_element(By.CLASS_NAME, "close")


if __name__ == '__main__':
    unittest.main()
      
