import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import Urls


@pytest.mark.usefixtures("driver")  # Подключаем фикстуру driver
class TestTabsNavigation:

    def is_tab_active(self, driver, active_tab_locator):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located(active_tab_locator))

    def test_go_to_sauces_section(self, driver):#Тест перехода к разделу 'Соусы'
        driver.get(Urls.HOME_PAGE)  # Открываем главную страницу

        # Нажимаем на вкладку "Соусы"
        sauces_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES_TAB))
        sauces_tab.click()

        # Проверяем, что вкладка "Соусы" активна (по новому классу current)
        assert self.is_tab_active(driver, Locators.ACTIVE_SAUCES_TAB), "Вкладка 'Соусы' не активна"

    def test_go_to_buns_section(self, driver):#Тест перехода к разделу 'Булки'.
        driver.get(Urls.HOME_PAGE)  # Открываем главную страницу

        # Нажимаем на вкладку "Соусы"
        sauces_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES_TAB))
        sauces_tab.click()

        # Нажимаем на вкладку "Булки"
        buns_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUNS_TAB))
        buns_tab.click()

        # Проверяем, что вкладка "Булки" активна (по новому классу current)
        assert self.is_tab_active(driver, Locators.ACTIVE_BUNS_TAB), "Вкладка 'Булки' не активна"

    def test_go_to_fillings_section(self, driver):#Тест перехода к разделу 'Начинки'."""
        driver.get(Urls.HOME_PAGE)  # Открываем главную страницу

        # Нажимаем на вкладку "Начинки"
        fillings_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.FILLINGS_TAB))
        fillings_tab.click()

        # Проверяем, что вкладка "Начинки" активна (по новому классу current)
        assert self.is_tab_active(driver, Locators.ACTIVE_FILLINGS_TAB), "Вкладка 'Начинки' не активна"