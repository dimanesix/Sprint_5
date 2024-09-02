from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data
import locators


class TestLogInAccount:
    def test_log_in_to_account_main_page(self, login):
        driver = login

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(test_data.MAIN_PAGE_URL))

        assert driver.current_url == test_data.MAIN_PAGE_URL and driver.find_element(By.XPATH, locators.BUTTON_SET_AN_ORDER)


    def test_button_personal_account_main_page(self):
        driver = webdriver.Chrome()

        driver.get(test_data.MAIN_PAGE_URL)

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, locators.BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(test_data.LOGIN_PAGE_URL))

        assert driver.current_url == test_data.LOGIN_PAGE_URL

        driver.quit()

    def test_button_enter_registration_page(self):
        driver = webdriver.Chrome()

        driver.get(test_data.REGISTRATION_PAGE_URL)

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, locators.BUTTON_LOGIN_REG_FORGOT_PWD).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(test_data.LOGIN_PAGE_URL))

        assert driver.current_url == test_data.LOGIN_PAGE_URL

        driver.quit()

    def test_button_enter_forgot_password_page(self):
        driver = webdriver.Chrome()

        driver.get(test_data.FORGOT_PASSWORD_PAGE)

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, locators.BUTTON_LOGIN_REG_FORGOT_PWD).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(test_data.LOGIN_PAGE_URL))

        assert driver.current_url == test_data.LOGIN_PAGE_URL

        driver.quit()
