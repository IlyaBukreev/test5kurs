from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthHelper:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get('https://www.saucedemo.com')
        login_input = self.driver.find_element(By.ID, 'user-name')
        login_input.send_keys(username)
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys(password)
        login_input.submit()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be('https://www.saucedemo.com/inventory.html')
        )

        return self.driver  # Возвращаем объект driver для цепочки вызовов
