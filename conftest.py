from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data
import locators
import pytest
import random


@pytest.fixture()
def login():
    driver = webdriver.Chrome()

    driver.get(test_data.MAIN_PAGE_URL)

    driver.delete_all_cookies()

    driver.find_element(By.XPATH, locators.BUTTON_LOG_IN_ACCOUNT).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, locators.AUTH_LOGIN_FORM)))

    driver.find_element(By.XPATH, locators.AUTH_EMAIL_FIELD).send_keys(test_data.VALID_EMAIL)

    driver.find_element(By.XPATH, locators.AUTH_PASSWORD_FIELD).send_keys(
        test_data.VALID_PASSWORD)

    driver.find_element(By.XPATH, locators.BUTTON_LOGIN_AUTH).click()

    return driver

@pytest.fixture()
def choose_sauces():
    driver = webdriver.Chrome()

    driver.get(test_data.MAIN_PAGE_URL)

    element = driver.find_element(By.XPATH, locators.SAUCES_SECTION)

    driver.execute_script(test_data.SCROLL_SCRIPT, element)

    return driver

@pytest.fixture()
def generate_email():
    valid_email = f'dmitriimitin13{random.randint(100, 999)}@yandex.ru'
    return valid_email


@pytest.fixture()
def generate_password():
    valid_password = f'{random.randint(100000, 999999)}'
    return valid_password
