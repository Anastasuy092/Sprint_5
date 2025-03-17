import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium import webdriver

def test_forgot_password_login(driver): #Тест переход по клику на "Личный кабинет"
    expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
    driver.get(Locators.HOME_PAGE_URL) # Используем URL главной страницы из локаторов

    # Нажимаем Войти в аккаунт
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    # Заполняем поля
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

    # Нажимаем кнопку Войти
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    # Нажимаем Личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

    # Ожидаем, пока URL страницы изменится на ожидаемый
    WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))

    # Проверяем, что текущий URL соответствует ожидаемому
    current_url = driver.current_url
    assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {current_url}"
    driver.quit()

def test_login_and_navigate_to_constructor(driver): # Тест переход по клику на Конструктор
    expected_url = "https://stellarburgers.nomoreparties.site/"
    driver.get(Locators.HOME_PAGE_URL)

    # Нажимаем Войти в аккаунтт
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    # Заполняем поля
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

    # Нажимаем кнопку Войти
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    # Нажимаем Личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
    # Нажимаем на элемент "Конструктор"
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_LINK)).click()

    # Ожидаем, пока URL страницы изменится на ожидаемый
    WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))

    # Проверяем, что текущий URL соответствует ожидаемому
    current_url = driver.current_url
    assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {current_url}"
    driver.quit()

def test_login_and_navigate_to_homepage(driver): # Тест переход по клику на Stellar Burgers
    expected_url = "https://stellarburgers.nomoreparties.site/"
    driver.get(Locators.HOME_PAGE_URL)

    # Нажимаем "Войти в аккаунт"
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    # Заполняем поля Email и Пароль
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

    # Нажимаем кнопку "Войти"
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

    # Нажимаем "Личный кабинет"
    driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()

    # Нажимаем на логотип Stellar Burgers (используем его XPATH)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO_LINK)).click()

    # Ожидаем, пока URL страницы изменится на ожидаемый (главную страницу)
    WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))

    # Проверяем, что текущий URL соответствует ожидаемому
    current_url = driver.current_url
    assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {current_url}"
    driver.quit()