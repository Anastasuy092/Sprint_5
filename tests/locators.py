from selenium.webdriver.common.by import By

class Locators:

    HOME_PAGE_URL = "https://stellarburgers.nomoreparties.site/"   # URL главной страницы

    # Локаторы для кнопок
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]") # Кнопка Войти в аккаунтт
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти"

    # Локаторы для полей ввода
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # Поле Пароль

    # Локаторы для ссылок и кнопок
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']") # Кнопка личный кабинет
    REGISTER_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']") # Кнопка Зарегистироваться
    LOGIN_FROM_REGISTRATION = (By.XPATH, "//a[text()='Войти']") # Кнопка Войти
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[contains(text(), "Восстановить пароль")]') # Кнопка Восстановить пароль
    LOGIN_FROM_FORGOT_PASSWORD = (By.XPATH, "//p[contains(text(), 'Вспомнили пароль?')]//a")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(), 'Конструктор')]") # Кнопка Конструктор
    LOGO_LINK = (By.XPATH, "/html/body/div[1]/div/header/nav/div/a") # Кнопка Stellar burgers
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.Account_button__14Yp3") # Кнопка выхода
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Для раздела Соусы
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div") # Для раздела Булки
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div") # Для раздела Начинки

    # Локатор для подтверждения входа
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
