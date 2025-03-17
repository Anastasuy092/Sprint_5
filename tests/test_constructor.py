import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium import webdriver

def test_go_to_sauces_section (driver): #Тест переход к разделу Соус
    driver.get(Locators.HOME_PAGE_URL)

    driver.find_element(*Locators.LOGIN_BUTTON).click()  # Нажимаем "Войти в аккаунтт"

    # Заполняем поля
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

    # Нажимаем кнопку Войти
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    # Нажимаем на вкладку "Соусы"
    sauces_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES_TAB))
    sauces_tab.click()

    # Проверяем, что вкладка "Соусы" активна
    active_sauces_tab = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SAUCES_TAB))
    assert active_sauces_tab is not None, "Вкладка 'Соусы' не активна"
    driver.quit()

def test_go_to_buns_section(driver): # тест переход к разделу БУлки
    driver.get(Locators.HOME_PAGE_URL)

    driver.find_element(*Locators.LOGIN_BUTTON).click()  # Нажимаем "Войти в аккаунт"

    # Заполняем поля
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

    # Нажимаем кнопку Войти
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    # Нажимаем Соус
    sauces_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES_TAB))
    sauces_tab.click()

    buns_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUNS_TAB))
    buns_tab.click()

    # Проверяем, что вкладка "Булки" активна
    active_buns_tab = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.BUNS_TAB))
    assert active_buns_tab is not None, "Вкладка 'Булки' не активна"
    driver.quit()

def test_go_to_fillings_section (driver): #Тест переход к разделу Начинки
    driver.get(Locators.HOME_PAGE_URL)

    driver.find_element(*Locators.LOGIN_BUTTON).click()  # Нажимаем "Войти в аккаунт"

    # Заполняем поля
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')

    # Нажимаем кнопку Войти
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    # Нажимаем Соус
    fillings_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.FILLINGS_TAB))
    fillings_tab.click()

    # Проверяем, что вкладка "Начинки" активна (имеет класс current)
    active_fillings_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab__') and contains(@class, 'current')]//span[text()='Начинки']")))
    assert active_fillings_tab is not None, "Вкладка 'Начинки' не активна"
    driver.quit()