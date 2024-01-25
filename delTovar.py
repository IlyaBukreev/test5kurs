import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
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

        add_to_cart_button = self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        add_to_cart_button.click()

        time.sleep(3)

        cart_badge_element = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
        self.assertEqual(cart_badge_element.text, '1', msg="Элемент корзины не отображает правильное количество товаров")

        add_to_cart_button = self.driver.find_element(By.ID, 'remove-sauce-labs-backpack')
        add_to_cart_button.click()

        time.sleep(3)

        # Проверка того, что элемент не отображается после нажатия
        try:
            cart_badge_element = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
            self.assertFalse(cart_badge_element.is_displayed(),
                             "Бейдж корзины не должен отображаться после добавления в корзину")
        except NoSuchElementException:
            # Исключение NoSuchElementException будет вызвано, если элемент не найден, что ожидается
            pass


if __name__ == '__main__':
    unittest.main()
