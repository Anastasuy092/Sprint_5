import sys
import os

# Добавляем корневую папку проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import generate_random_email, login


@pytest.mark.usefixtures("driver")  # Подключаем фикстуру driver
class TestNavigationForgotPasswordLogin:

    def test_forgot_password_login(self, driver):
        #Тест переход по клику на 'Личный кабинет'.
        expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
        login(driver)  # Выполняем авторизацию

        # Нажимаем "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        # Ожидаем, пока URL страницы изменится на ожидаемый
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))

        # Проверяем, что текущий URL соответствует ожидаемому
        current_url = driver.current_url
        assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {current_url}"

@pytest.mark.usefixtures("driver")  # Подключаем фикстуру driver
class TestLoginAndNavigateToConstructor:

    def test_login_and_navigate_to_constructor(self, driver):
        #Тест переход по клику на 'Конструктор'.
        expected_url = "https://stellarburgers.nomoreparties.site/"
        login(driver)  # Выполняем авторизацию

        # Нажимаем "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        # Нажимаем на элемент "Конструктор"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_LINK)).click()

        # Ожидаем, пока URL страницы изменится на ожидаемый
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))

        # Проверяем, что текущий URL соответствует ожидаемому
        current_url = driver.current_url
        assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {current_url}"

@pytest.mark.usefixtures("driver")  # Подключаем фикстуру driver
class TestLoginAndNavigateToHomepage:

    def test_login_and_navigate_to_homepage(self, driver):
        #Тест переход по клику на 'Stellar Burgers'.
        expected_url = "https://stellarburgers.nomoreparties.site/"
        login(driver)  # Выполняем авторизацию

        # Нажимаем "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        # Нажимаем на логотип Stellar Burgers
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO_LINK)).click()

        # Ожидаем, пока URL страницы изменится на ожидаемый
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))

        # Проверяем, что текущий URL соответствует ожидаемому
        current_url = driver.current_url
        assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {current_url}"