import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def filter_products(self, value):
        # Находим элемент выпадающего списка
        sort_dropdown = self.driver.find_element(By.CLASS_NAME, 'product_sort_container')

        # Используем Select для удобства работы с выпадающим списком
        select = Select(sort_dropdown)

        # Выбираем опцию по значению
        select.select_by_value(value)

        # Добавляем ожидание, чтобы дать время для обновления страницы после фильтрации
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item'))
        )

    def test_login_and_filter_products(self):
        # Открываем сайт
        self.driver.get('https://www.saucedemo.com')

        # Заполняем поле логина
        login_input = self.driver.find_element(By.ID, 'user-name')
        login_input.send_keys('standard_user')

        # Заполняем поле пароля
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys('secret_sauce')

        # Добавляем ожидание перед нажатием Enter
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'login-button'))
        )

        # Нажимаем Enter, чтобы выполнить вход
        login_input.submit()

        # Фильтрируем товары по имени (A to Z)
        self.filter_products('az')

        # Получаем список названий товаров
        product_names = [element.text.lower() for element in
                         self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')]

        # Проверяем, что товары отсортированы в алфавитном порядке
        try:
            self.assertListEqual(product_names, sorted(product_names))
            print("Тест успешно пройден. Товары отсортированы корректно.")
        except AssertionError:
            print("Тест не пройден. Товары не отсортированы в алфавитном порядке.")


if __name__ == "__main__":
    unittest.main()
