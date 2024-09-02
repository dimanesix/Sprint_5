from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data
import locators


class TestPersonalAccount:
    def test_enter_to_personal_account(self, login):
        driver = login

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, locators.HEADER_NAV_PANEL)))

        driver.find_element(By.XPATH, locators.BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(test_data.PROFILE_PAGE_URL))

        assert driver.current_url == test_data.PROFILE_PAGE_URL


    def test_click_on_constructor(self, login):
        driver = login

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, locators.HEADER_NAV_PANEL)))

        driver.find_element(By.XPATH, locators.BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, locators.HEADER_NAV_PANEL)))

        driver.find_element(By.XPATH, locators.BUTTON_CONSTRUCTOR).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(test_data.MAIN_PAGE_URL))

        assert driver.current_url == test_data.MAIN_PAGE_URL

    def test_click_on_logo(self, login):
        driver = login

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, locators.HEADER_NAV_PANEL)))

        driver.find_element(By.XPATH, locators.LOGO_STELLAR_BURGERS).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(test_data.MAIN_PAGE_URL))

        assert driver.current_url == test_data.MAIN_PAGE_URL
