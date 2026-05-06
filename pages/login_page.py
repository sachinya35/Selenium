from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    username_id = (By.ID, "user-name")
    password_id = (By.ID, "password")
    login_id=(By.ID,"login-button")
    def websites(self,url):
        loaded=(By.XPATH,"//div[@class='login_logo']")
        self.driver.get(url)
        assert self.wait.until(EC.visibility_of_element_located(loaded)),\
            "Page not loaded"
    def login(self,username,password,want):
        self.driver.find_element(*self.username_id).send_keys(username)
        self.driver.find_element(*self.password_id).send_keys(password)
        self.driver.find_element(*self.login_id).click()
        self.wait.until(EC.url_to_be(want))
        response = requests.get(want)
        if response.status_code == 200:
            print("Page is reachable")


