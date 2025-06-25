from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#Конструктор

class TestBooksCollector4:
    def test_button_constructor_coys(self, driver, auth): 
        driver.find_element(By.XPATH, "//div/span[text()='Соусы']").click()
        WebDriverWait(driver, 10)
        rd = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current__')]/span[@class='text text_type_main-default']")
        assert rd.text == 'Соусы'


    def test_button_construktor_nachinki(self, driver, auth):

        driver.find_element(By.XPATH, "//div/span[text()='Начинки']").click()
        WebDriverWait(driver, 10)
        rd = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current__')]/span[@class='text text_type_main-default']")
        assert rd.text == 'Начинки'


    def test_button_construktor_boolki(self, driver, auth):

        driver.find_element(By.XPATH, "//div/span[text()='Соусы']").click()
        WebDriverWait(driver, 10)
        driver.find_element(By.XPATH, "//div/span[text()='Булки']").click()
        WebDriverWait(driver, 10)
        rd = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current__')]/span[@class='text text_type_main-default']")
        assert rd.text == 'Булки'

