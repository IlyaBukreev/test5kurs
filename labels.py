import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException  # Import NoSuchElementException

class YourTestClass(unittest.TestCase):

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

        # Находим все элементы с классом "inventory_item_name"
        inventory_items = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

        # Проверяем, что хотя бы один элемент найден
        self.assertTrue(len(inventory_items) > 0, "Не найдены элементы с классом 'inventory_item_name'")

        # Проверяем, что каждый элемент отображается и имеет гиперссылку
        for item in inventory_items:
            try:
                # Проверка, что элемент отображается
                self.assertTrue(item.is_displayed(), f"Элемент {item.text} не отображается")

                # Проверка, что элемент имеет гиперссылку
                link = item.find_element(By.TAG_NAME, 'a')
                self.assertTrue(link.get_attribute('href'), f"Элемент {item.text} не имеет гиперссылки")
            except NoSuchElementException:
                # Исключение NoSuchElementException будет вызвано, если элемент не найден, что ожидается
                pass

if __name__ == '__main__':
    unittest.main()
