from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data


class TestPersonalAccount:
    def test_jump_to_personal_account(self):
        driver = webdriver.Chrome()

        driver.get(test_data.MAIN_PAGE_URL)

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, './/button[text()="Войти в аккаунт"]').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, 'Auth_login__3hAey')))

        driver.find_element(By.XPATH, './/div[@class="input pr-6 pl-6 input_type_text '
                                      'input_size_default"]/input[@class="text input__textfield '
                                      'text_type_main-default"]').send_keys(test_data.VALID_EMAIL)

        driver.find_element(By.XPATH, './/div[@class="input pr-6 pl-6 input_type_password input_size_default"]/input['
                                      '@class="text input__textfield text_type_main-default"]').send_keys(
            test_data.VALID_PASSWORD)

        driver.find_element(By.XPATH, './/button[text()="Войти"]').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, 'AppHeader_header__nav__g5hnF')))

        driver.find_element(By.XPATH, './/p[text()="Личный Кабинет"]/parent::a').click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(test_data.PROFILE_PAGE_URL))

        assert driver.current_url == test_data.PROFILE_PAGE_URL

        driver.quit()

    def jump_to_constructor_and_logo(self):
        driver = webdriver.Chrome()

        driver.get(test_data.MAIN_PAGE_URL)

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, './/button[text()="Войти в аккаунт"]').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, 'Auth_login__3hAey')))

        driver.find_element(By.XPATH, './/div[@class="input pr-6 pl-6 input_type_text '
                                      'input_size_default"]/input[@class="text input__textfield '
                                      'text_type_main-default"]').send_keys(test_data.VALID_EMAIL)

        driver.find_element(By.XPATH, './/div[@class="input pr-6 pl-6 input_type_password input_size_default"]/input['
                                      '@class="text input__textfield text_type_main-default"]').send_keys(
            test_data.VALID_PASSWORD)

        driver.find_element(By.XPATH, './/button[text()="Войти"]').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, 'AppHeader_header__nav__g5hnF')))

        driver.find_element(By.XPATH, './/p[text()="Личный Кабинет"]/parent::a').click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, 'AppHeader_header__X9aJA')))

        driver.find_element(By.XPATH, './/p[@class="AppHeader_header__linkText__3q_va ml-2"][text('
                                      ')="Конструктор"]/parent::a').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(test_data.MAIN_PAGE_URL))

        assert driver.current_url == test_data.MAIN_PAGE_URL

        driver.quit()
