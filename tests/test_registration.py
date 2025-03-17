import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_successful_registration(driver):  # Тест успешной регистрации
    driver.get(Locators.HOME_PAGE_URL)  # Используем URL главной страницы из локаторов

    driver.find_element(*Locators.LOGIN_BUTTON).click()  # Кнопка "Войти в аккаунт"
    driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()  # Нажимаем "Зарегистрироваться"

    # Заполняем поля
    driver.find_element(By.NAME, "name").send_keys("Анастасия")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys("Anastasuy_Bazq99we_19_123@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")

    # Нажимаем кнопка "Зарегистрироваться"
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    # Ожидаем появления кнопки "Войти", чтобы убедиться, что регистрация прошла успешно
    success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Вход']")))
    assert success_message is not None, "Регистрация не удалась!"

    driver.quit()

def test_invalid_password_registration(driver):  # Ошибка для некорректного пароля
    driver.get(Locators.HOME_PAGE_URL)  # Используем URL главной страницы из локаторов

    driver.find_element(*Locators.LOGIN_BUTTON).click()  # Кнопка "Войти в аккаунт"
    driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()  # Нажимаем "Зарегистрироваться"

    # Заполняем поля
    driver.find_element(By.NAME, "name").send_keys("Анастасия")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys("Anastasuy_Bazova_19_123@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123")  # Некорректный пароль (слишком короткий)

    # Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    # Ожидаем появления ошибки
    error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "input__error")))
    assert error_message.text == "Некорректный пароль"

    driver.quit()


