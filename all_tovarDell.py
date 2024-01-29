import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException


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

        # Найти все элементы с классом 'btn_inventory' и добавить в корзину
        add_to_cart_buttons = self.driver.find_elements(By.CLASS_NAME, 'btn_inventory')
        for button in add_to_cart_buttons:
            button.click()
            time.sleep(3)

        # Найти все элементы с классом 'btn_secondary' (удаление товаров) и убрать из корзины
        remove_buttons = self.driver.find_elements(By.CLASS_NAME, 'btn_secondary')
        for remove_button in remove_buttons:
            remove_button.click()
            time.sleep(3)

            # Проверка того, что элемент не отображается после нажатия
            try:
                cart_badge_element = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
                self.assertTrue(cart_badge_element.is_displayed(),
                                 "Бейдж корзины не должен отображаться после добавления в корзину")
            except NoSuchElementException:
                # Исключение NoSuchElementException будет вызвано, если элемент не найден, что ожидается
                pass


if __name__ == '__main__':
    unittest.main()
