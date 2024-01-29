import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login_with_valid_credentials(self):
        self.driver.get('https://www.saucedemo.com')
        login_input = self.driver.find_element(By.ID, 'user-name')
        login_input.send_keys('standard_user')
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys('secret_sauce')
        login_input.submit()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be('https://www.saucedemo.com/inventory.html')
        )

        # Найти все элементы с указанным классом
        add_to_cart_buttons = self.driver.find_elements(By.CLASS_NAME, 'btn_inventory')

        # Нажать на каждый элемент
        for button in add_to_cart_buttons:
            button.click()
            time.sleep(3)

        cart_badge_element = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
        # Проверить количество товаров в значке корзины
        self.assertEqual(cart_badge_element.text, str(len(add_to_cart_buttons)),
                         msg="Элемент корзины не отображает правильное количество товаров")


if __name__ == '__main__':
    unittest.main()
