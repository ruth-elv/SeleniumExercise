import pytest
import unittest
from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegister(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_success_register(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com")
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-female").click()
        #pilih = Select(driver.find_element(By.ID, "gender-female"))
        #pilih.select_by_value('F')
        driver.find_element(By.ID, "FirstName").send_keys("Ruth")
        driver.find_element(By.ID, "LastName").send_keys("El")
        driver.find_element(By.ID, "Email").send_keys("email@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("pass1234")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("pass1234")
        driver.find_element(By.ID, "register-button").click()

        respon = driver.find_element(By.CSS_SELECTOR, ".center-2").text
        self.assertIn("Register", respon)
        driver.minimize_window()

    def test_b_failed_register(self):
        driver = self.browser
        driver.get("https://demowebshop.tricentis.com")
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        driver.find_element(By.ID, "gender-male").click()
        #pilih = Select(driver.find_element(By.ID, "gender-female"))
        #pilih.select_by_value('F')
        driver.find_element(By.ID, "FirstName").send_keys("Rudi")
        driver.find_element(By.ID, "LastName").send_keys("Tabuti")
        driver.find_element(By.ID, "Email").send_keys("r@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("pass1234")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("pass1234")
        driver.find_element(By.ID, "register-button").click()
        respon = driver.find_element(By.CLASS_NAME, "validation-summary-errors")
        driver.minimize_window()

    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main()