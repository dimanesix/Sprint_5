from selenium.webdriver.common.by import By
from selenium import webdriver
import test_data
import locators


class TestConstructorForm:

    def test_jump_to_sauces(self, choose_sauces):
        driver = choose_sauces

        assert test_data.ACTIVE_SECTION in driver.find_element(By.XPATH, locators.SAUCES).get_attribute('class')

        driver.quit()

    def test_jump_to_bread(self, choose_sauces):
        driver = choose_sauces

        element = driver.find_element(By.XPATH, locators.BREAD_SECTION)

        driver.execute_script(test_data.SCROLL_SCRIPT, element)

        assert test_data.ACTIVE_SECTION in driver.find_element(By.XPATH, locators.BREAD).get_attribute('class')

        driver.quit()

    def test_jump_to_topping(self):
        driver = webdriver.Chrome()

        driver.get(test_data.MAIN_PAGE_URL)

        element = driver.find_element(By.XPATH, locators.TOPING_SECTION)

        driver.execute_script(test_data.SCROLL_SCRIPT, element)

        assert test_data.ACTIVE_SECTION in driver.find_element(By.XPATH, locators.TOPPING).get_attribute('class')

        driver.quit()
