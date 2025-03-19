from selenium.webdriver.common.by import By

class Locators:

    # Локаторы для кнопок
    LOGIN_BUTTON = (
    By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg") # Кнопка Войти в аккаунтт
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa')]") # Кнопка "Войти"

    # Локаторы для полей ввода
    EMAIL_INPUT = (By.XPATH, "//label[contains(@class, 'input__placeholder') and text()='Email']/following-sibling::input") # Поле Email
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input.input__textfield[type='password']") # Поле Пароль

    # Локаторы для ссылок и кнопок
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']") # Кнопка личный кабинет
    REGISTER_LINK = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Зарегистрироваться']")  # Ссылка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    LOGIN_FROM_REGISTRATION = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']") # Кнопка Войти на форме регистрации
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and contains(text(), 'Восстановить пароль')]") # Кнопка Восстановить пароль
    LOGIN_FROM_FORGOT_PASSWORD = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and @href='/login']") # Кнопка Войти на форме восстановления пароля
    CONSTRUCTOR_LINK =  (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va')]") # Кнопка Конструктор
    LOGO_LINK = (By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2 a") # Кнопка Stellar burgers
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']") # Кнопка выхода в личном кабинете
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Соусы']") # Для раздела Соусы
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Булки']")# Для раздела Булки
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Начинки']")# Для раздела Начинки
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")   # Локатор для подтверждения входа

  # Локаторы для проверки активных вкладок
    ACTIVE_SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'current')]//span[text()='Соусы']")
    ACTIVE_BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Булки']")
    ACTIVE_FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Начинки']")