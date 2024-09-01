from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data
import locators


class TestRegistrationForm:
    def test_user_registration_with_correct_data(self, generate_email, generate_password):
        driver = webdriver.Chrome()

        driver.get(test_data.REGISTRATION_PAGE_URL)

        driver.delete_all_cookies()

        name_email_el = driver.find_elements(By.XPATH, locators.REG_NAME_EMAIL_FIELD)
        name_email_el[0].send_keys(test_data.VALID_NAME)
        name_email_el[1].send_keys(generate_email)

        driver.find_element(By.XPATH, locators.REG_PASSWORD_FIELD).send_keys(generate_password)

        driver.find_element(By.XPATH, locators.BUTTON_REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(test_data.LOGIN_PAGE_URL))

        assert driver.current_url == test_data.LOGIN_PAGE_URL

        driver.quit()

    def test_error_message_for_incorrect_password(self):
        driver = webdriver.Chrome()

        driver.get(test_data.REGISTRATION_PAGE_URL)

        driver.find_element(By.XPATH, locators.REG_PASSWORD_FIELD).send_keys(test_data.ONE_SYMBOL_PASSWORD)

        driver.find_element(By.XPATH, locators.BUTTON_REGISTER).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, locators.PLACE_FOR_ERROR_PWD_MESSAGE)))

        assert driver.find_element(By.CLASS_NAME, locators.ERROR_PWD_MESSAGE).text == test_data.ERROR_TEXT_FOR_INCORRECT_PWD

        driver.quit()
