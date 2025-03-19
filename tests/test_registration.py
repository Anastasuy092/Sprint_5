import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import generate_random_email
from urls import Urls

@pytest.mark.usefixtures("driver")  # Подключаем фикстуру driver
class TestRegistration:

    def test_successful_registration(self, driver):  # Тест успешной регистрации
        driver.get(Urls.HOME_PAGE)  # Используем URL главной страницы из локаторов

        driver.find_element(*Locators.LOGIN_BUTTON).click()  # Кнопка "Войти в аккаунт"
        driver.find_element(*Locators.REGISTER_LINK).click()  # Нажимаем "Зарегистрироваться"

        # Генерируем случайный email
        random_email = generate_random_email()

        # Заполняем поля
        driver.find_element(By.NAME, "name").send_keys("Анастасия")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(random_email)  # Используем сгенерированный email
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")

        # Нажимаем кнопку "Зарегистрироваться"
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Ожидаем появления кнопки "Войти", чтобы убедиться, что регистрация прошла успешно
        success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        assert success_message is not None, "Регистрация не удалась!"

    def test_invalid_password_registration(self, driver):  # Ошибка для некорректного пароля
        driver.get(Urls.HOME_PAGE)  # Используем URL главной страницы из локаторов

        driver.find_element(*Locators.LOGIN_BUTTON).click()  # Кнопка "Войти в аккаунт"
        driver.find_element(*Locators.REGISTER_LINK).click()  # Нажимаем "Зарегистрироваться"

        # Генерируем случайный email
        random_email = generate_random_email()

        # Заполняем поля
        driver.find_element(By.NAME, "name").send_keys("Анастасия")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(random_email)  # Используем сгенерированный email
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123")  # Некорректный пароль (слишком короткий)

        # Нажимаем кнопку "Зарегистрироваться"
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Ожидаем появления ошибки
        error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "input__error")))
        assert error_message.text == "Некорректный пароль"

        driver.quit()


