import pytest
import random

@pytest.fixture()
def generate_email():
    valid_email = f'dmitriimitin13{random.randint(100,999)}@yandex.ru'
    return valid_email

@pytest.fixture()
def generate_password():
    valid_password = f'{random.randint(100000,999999)}'
    return valid_password