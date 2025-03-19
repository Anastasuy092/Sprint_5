import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import Urls


@pytest.mark.usefixtures("driver")  # Подключаем фикстуру driver
class TestNavigation:

    def login(self, driver):
        #Выполняет авторизацию пользователя.
        driver.get(Urls.HOME_PAGE)
        driver.find_element(*Locators.LOGIN_BUTTON).click()  # Нажимаем "Войти в аккаунт"

        # Заполняем поля
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    def test_forgot_password_login(self, driver):
        #Тест переход по клику на 'Личный кабинет'.
        expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
        self.login(driver)  # Выполняем авторизацию

        # Нажимаем "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        # Ожидаем, пока URL страницы изменится на ожидаемый
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))

        # Проверяем, что текущий URL соответствует ожидаемому
        current_url = driver.current_url
        assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {current_url}"

    def test_login_and_navigate_to_constructor(self, driver):
        #Тест переход по клику на 'Конструктор'.
        expected_url = "https://stellarburgers.nomoreparties.site/"
        self.login(driver)  # Выполняем авторизацию

        # Нажимаем "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        # Нажимаем на элемент "Конструктор"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_LINK)).click()

        # Ожидаем, пока URL страницы изменится на ожидаемый
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))

        # Проверяем, что текущий URL соответствует ожидаемому
        current_url = driver.current_url
        assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {current_url}"

    def test_login_and_navigate_to_homepage(self, driver):
        #Тест переход по клику на 'Stellar Burgers'.
        expected_url = "https://stellarburgers.nomoreparties.site/"
        self.login(driver)  # Выполняем авторизацию

        # Нажимаем "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

        # Нажимаем на логотип Stellar Burgers
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO_LINK)).click()

        # Ожидаем, пока URL страницы изменится на ожидаемый
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))

        # Проверяем, что текущий URL соответствует ожидаемому
        current_url = driver.current_url
        assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {current_url}"