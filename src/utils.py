import random
import string
import os
import re
from faker import Faker


BASE_URL = 'https://qa-desk.stand.praktikum-services.ru/'

# генерируем email и пароль, сохраняем в файл
def generate_credentials(filename='credentials.txt'):
    home_dir = os.path.expanduser('~')
    full_path = os.path.join(home_dir, filename)

    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(['gmail.com', 'mail.ru', 'yandex.ru'])
    email = f'{username}@{domain}'

    password = ''.join(random.choice(string.ascii_letters + string.digits + '!@#$%^&*') for _ in range(12))

    with open(full_path, 'a') as f:
        f.write(f'Email: {email}\tPassword: {password}\n')

    return email, password


# генерируем email не по маске *******@*******.***
def invalid_email():
    email = ''.join(random.choice(string.ascii_lowercase) for _ in range(12))
    return email


# проверяем является ли цвет красным
def is_error_red(element, min_red=200, max_green=120, max_blue=120):
    def get_color(element, css_property="color"):
        try:
            return element.value_of_css_property(css_property)
        except:
            return None

    def check_color(color):
        if not color:
            return False

        rgb_match = re.match(r'rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)', color)
        if rgb_match:
            r, g, b = map(int, rgb_match.groups())
            return r >= min_red and g <= max_green and b <= max_blue
        return False

    color = get_color(element)
    border_color = get_color(element, "border-color")
    return check_color(color) or check_color(border_color)


# генерируем заголовок, описание и цену объявления
def generate_ad_data():
    fake = Faker('ru_RU')

    title = fake.catch_phrase()
    description = fake.paragraph(nb_sentences=3)
    price = random.randint(9999, 99999)

    return  title, description, str(price)
