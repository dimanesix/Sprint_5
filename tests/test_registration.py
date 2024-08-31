from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data


class TestRegistrationForm:
    def test_user_registration_with_correct_data(self, generate_email, generate_password):
        driver = webdriver.Chrome()

        driver.get(test_data.REGISTRATION_PAGE_URL)

        driver.delete_all_cookies()

        name_email_el = driver.find_elements(By.XPATH,
                                             './/div[@class="input pr-6 pl-6 input_type_text '
                                             'input_size_default"]/input[@class="text input__textfield '
                                             'text_type_main-default"]')
        name_email_el[0].send_keys(test_data.VALID_NAME)
        name_email_el[1].send_keys(generate_email)

        driver.find_element(By.XPATH,
                            './/div[@class="input pr-6 pl-6 input_type_password input_size_default"]/input['
                            '@class="text input__textfield text_type_main-default"]').send_keys(
            generate_password)
        driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(test_data.LOGIN_PAGE_URL))

        assert driver.current_url == test_data.LOGIN_PAGE_URL

        driver.quit()

    def test_error_message_for_incorrect_password(self):
        driver = webdriver.Chrome()

        driver.get(test_data.REGISTRATION_PAGE_URL)

        driver.find_element(By.XPATH,
                            './/div[@class="input pr-6 pl-6 input_type_password input_size_default"]/input['
                            '@class="text input__textfield text_type_main-default"]').send_keys(
            test_data.ONE_SYMBOL_PASSWORD)

        driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'input_status_error')))

        assert driver.find_element(By.CLASS_NAME, 'input__error').text == test_data.ERROR_TEXT_FOR_INCORRECT_PWD

        driver.quit()
