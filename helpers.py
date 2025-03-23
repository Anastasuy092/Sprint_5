import random
import string
from locators import Locators
from urls import Urls


def generate_random_email():
    #Генерирует случайный email для регистрации
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_string}@yandex.ru"

def login(driver):
    driver.get(Urls.HOME_PAGE)  # Переходим на главную страницу
    driver.find_element(*Locators.LOGIN_BUTTON).click()  # Нажимаем "Войти в аккаунт"
    # Заполняем поля
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('Anastasuy_Bazova_19_123@yandex.ru')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')
    # Нажимаем кнопку "Войти"
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()