import sys
import os

# Добавляем корневую папку проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium import webdriver
from urls import Urls
from helpers import generate_random_email, login

@pytest.mark.usefixtures("driver")
class TestLoginFromMainPage:

    def test_login_from_main_page(self, driver):  # Тест входа по кнопке "Войти в аккаунтт"
        driver.get(Urls.HOME_PAGE)  # Используем URL главной страницы из локаторов

        driver.find_element(*Locators.LOGIN_BUTTON).click()  # Нажимаем "Войти в аккаунт"

    # Заполняем поля
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

    # Нажимаем кнопку Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    # Ожидаем появления элемента, подтверждающего успешный вход
        personal_account = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT))

    # Проверяем, что элемент "Личный Кабинет" отображается на странице
        assert personal_account.is_displayed(), "Не удалось войти в аккаунт"

@pytest.mark.usefixtures("driver")
class TestLoginViaPersonalAccount:

    def test_login_via_personal_account(self, driver):  # Тест входа через личный кабинет
        driver.get(Urls.HOME_PAGE)  # Используем URL главной страницы из локаторов

        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()  # Нажимаем Личный кабинет

    # Заполняем поля
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

    # Нажимаем кнопку Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    # Ожидаем появления элемента, подтверждающего успешный вход
        personal_account = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT))

    # Проверяем, что элемент "Личный Кабинет" отображается на странице
        assert personal_account.is_displayed(), "Не удалось войти в аккаунт"

@pytest.mark.usefixtures("driver")
class TestLoginViaRegistrationForm:

    def test_login_via_registration_form(self,driver):  # Тест входа через кнопку в форме регистрации
        driver.get(Urls.HOME_PAGE)  # Используем URL главной страницы из локаторов

        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()  # Нажимаем Личный кабинет
        driver.find_element(*Locators.REGISTER_LINK).click()  # Нажимаем Зарегистрироваться
        driver.find_element(*Locators.LOGIN_FROM_REGISTRATION).click()  # Нажимаем кнопку Войти

    # Заполняем поля
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

    # Нажимаем кнопку Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    # Ожидаем появления элемента, подтверждающего успешный вход
        personal_account = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT))

    # Проверяем, что элемент "Личный Кабинет" отображается на странице
        assert personal_account.is_displayed(), "Не удалось войти в аккаунт"

@pytest.mark.usefixtures("driver")
class TestForgotPasswordLogin:

    def test_forgot_password_login(self,driver):  # Тест входа через кнопку в форме восстановления пароля
        driver.get(Urls.HOME_PAGE)  # Используем URL главной страницы из локаторов

        driver.find_element(*Locators.LOGIN_BUTTON).click()  # Нажимаем Войти в аккаунт
        driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()  # Нажимаем Восстановить пароль
        driver.find_element(*Locators.LOGIN_FROM_FORGOT_PASSWORD).click()  # Нажимаем Войти

    # Заполняем поля
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

    # Нажимаем кнопку Войти
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    # Ожидаем появления элемента, подтверждающего успешный вход
        personal_account = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT))

    # Проверяем, что элемент "Личный Кабинет" отображается на странице
        assert personal_account.is_displayed(), "Не удалось войти в аккаунт"
