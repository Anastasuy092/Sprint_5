import random
import string

def generate_random_email():
    #Генерирует случайный email для регистрации
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_string}@yandex.ru"