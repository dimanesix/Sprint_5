from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data
import locators


class TestLogoutAccount:
    def test_logout_from_account(self, login):
        driver = login

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, locators.HEADER_NAV_PANEL)))

        driver.find_element(By.XPATH, locators.BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(test_data.PROFILE_PAGE_URL))

        driver.find_element(By.XPATH, locators.BUTTON_EXIT_FROM_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(test_data.LOGIN_PAGE_URL))

        assert driver.current_url == test_data.LOGIN_PAGE_URL

        driver.quit()
