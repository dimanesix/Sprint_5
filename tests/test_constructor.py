from selenium.webdriver.common.by import By
from selenium import webdriver
import test_data


class TestConstructorForm:

    def test_jump_to_sauces(self):
        driver = webdriver.Chrome()

        driver.get(test_data.MAIN_PAGE_URL)

        driver.delete_all_cookies()

        element = driver.find_element(By.XPATH, './/h2[text()="Соусы"]')

        driver.execute_script("arguments[0].scrollIntoView();", element)

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH,
                                                                    './/span[text()="Соусы"]/parent::div').get_attribute(
            'class')

        driver.quit()
    def test_jump_to_bread(self):
        driver = webdriver.Chrome()

        driver.get(test_data.MAIN_PAGE_URL)

        driver.delete_all_cookies()

        element = driver.find_element(By.XPATH, './/h2[text()="Соусы"]')

        driver.execute_script("arguments[0].scrollIntoView();", element)

        element = driver.find_element(By.XPATH, './/h2[text()="Булки"]')

        driver.execute_script("arguments[0].scrollIntoView();", element)

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH,
                                                                    './/span[text()="Булки"]/parent::div').get_attribute(
            'class')

        driver.quit()

    def test_jump_to_topping(self):
        driver = webdriver.Chrome()

        driver.get(test_data.MAIN_PAGE_URL)

        driver.delete_all_cookies()

        element = driver.find_element(By.XPATH, './/h2[text()="Начинки"]')

        driver.execute_script("arguments[0].scrollIntoView();", element)

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH,
                                                                    './/span[text()="Начинки"]/parent::div').get_attribute(
            'class')

        driver.quit()