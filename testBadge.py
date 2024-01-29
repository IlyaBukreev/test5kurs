import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

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

            # Проверить изменение класса shopping_cart_badge после добавления товара
            cart_badge_element = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
            self.assertNotEqual(cart_badge_element.text, '0', msg="Корзина пуста после добавления товара")

        # Найти все элементы с классом 'btn_secondary' (удаление товаров) и убрать из корзины
        remove_buttons = self.driver.find_elements(By.CLASS_NAME, 'btn_secondary')
        for remove_button in remove_buttons:
            remove_button.click()
            time.sleep(3)

        # Проверить, что корзина пуста (shopping_cart_link не отображается)
        cart_link = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        is_cart_link_displayed = cart_link.is_displayed()
        self.assertFalse(is_cart_link_displayed, msg="Корзина не пуста после удаления всех товаров")


if __name__ == '__main__':
    unittest.main()
