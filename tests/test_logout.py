import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import Urls

@pytest.mark.usefixtures("driver")  # Подключаем фикстуру driver
class TestLogout:

    def login(self, driver):
        #Выполняет авторизацию пользователя."""
        driver.get(Urls.HOME_PAGE)
        driver.find_element(*Locators.LOGIN_BUTTON).click()  # Нажимаем "Войти в аккаунт"

        # Заполняем поля
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    def test_logout(self, driver):
        #Тест выхода из аккаунта.
        expected_login_url = "https://stellarburgers.nomoreparties.site/login"
        self.login(driver)  # Выполняем авторизацию

        # Нажимаем "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        # Нажимаем кнопку "Выход"
        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        # Ожидаем редиректа на страницу логина
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_login_url))

        # Проверяем, что текущий URL — это страница входа
        current_url = driver.current_url
        assert current_url == expected_login_url, f"Ожидаемый URL: {expected_login_url}, Фактический URL: {current_url}"