from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data


class TestLogoutAccount:
    def test_logout_from_account(self):
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

        driver.find_element(By.XPATH, './/button[text()="Выход"]').click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(test_data.LOGIN_PAGE_URL))

        assert driver.current_url == test_data.LOGIN_PAGE_URL

        driver.quit()
