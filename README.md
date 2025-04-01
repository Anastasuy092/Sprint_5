# Sprint_5
# Проект автоматизации тестирования Stellar Burgers

## Описание проекта
Проект содержит автоматизированные тесты для веб-приложения Stellar Burgers.
Автотесты написаны с использованием Python и Selenium WebDrive*, а для управления тестами применяется pytest.

## Требования
- Python 3.10+
- Google Chrome / Mozilla Firefox
- Chromedriver / Geckodriver (для соответствующего браузера))

## Запуск тестов
Для запуска всех тестов выполните команду:

pytest -v

## Структура проекта

│-- tests/                    # Папка с тестами
│   ├── test_login.py         # Тесты авторизации
│   ├── test_registration.py  # Тесты входа
│   ├── test_profile.py       # Тесты Переход в личный кабинет и Переход из личного кабинета в конструктор
│   ├── test_logout.py        # Тест выход из аккаунта
│   ├── test_constructor.py   # Тесты раздела Конструктор
│-- locators.py               # Файл с локаторами элементов
│-- conftest.py               # Фикстуры для pytest
│-- README.md                 # Документация проекта


## Контакты
Если у вас есть вопросы или предложения, свяжитесь со мной через GitHub или почту

