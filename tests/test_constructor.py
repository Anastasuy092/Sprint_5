import sys
import os
# Добавляем корневую папку проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import Urls


@pytest.mark.usefixtures("driver")  # Подключаем фикстуру driver
class TestBunsNavigation:

    def test_go_to_sauces_section(self, driver):#Тест перехода к разделу 'Соусы'
        driver.get(Urls.HOME_PAGE)  # Открываем главную страницу

        # Нажимаем на вкладку "Соусы"
        sauces_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAUCES_TAB))
        sauces_tab.click()

        # Проверяем, что вкладка "Соусы" активна (по классу current)
        active_sauces_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SAUCES_TAB)
        )

        # Проверяем, что текст активной вкладки соответствует "Соусы"
        assert active_sauces_tab.text == 'Соусы', f"Ожидался текст 'Соусы', но получен '{active_sauces_tab.text}'"

    def test_go_to_buns_section(self, driver):#Тест перехода к разделу 'Булки'.
        driver.get(Urls.HOME_PAGE)  # Открываем главную страницу

        # Нажимаем на вкладку "БУлки"
        sauces_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES_TAB))
        sauces_tab.click()

        # Нажимаем на вкладку "Булки"
        buns_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUNS_TAB))
        buns_tab.click()

        # Проверяем, что вкладка "Булки" активна (по новому классу current)
        active_buns_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_BUNS_TAB)
        )
        # Проверяем, что текст активной вкладки соответствует "Булки"
        assert active_buns_tab.text == 'Булки', f"Ожидался текст 'Булки', но получен '{active_buns_tab.text}'"

    def test_go_to_fillings_section(self, driver):#Тест перехода к разделу 'Начинки'.
        driver.get(Urls.HOME_PAGE)  # Открываем главную страницу

        # Нажимаем на вкладку "Начинки"
        fillings_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.FILLINGS_TAB))
        fillings_tab.click()

        # Проверяем, что вкладка "Начинки" активна (по новому классу current)
        active_fillings_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_FILLINGS_TAB)
        )
        # Проверяем, что текст активной вкладки соответствует "Начинки"
        assert active_fillings_tab.text == 'Начинки', f"Ожидался текст 'Начинки', но получен '{active_fillings_tab.text}'"