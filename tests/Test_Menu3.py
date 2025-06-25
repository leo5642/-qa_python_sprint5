from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#Переход в личный кабинет 

class TestBooksCollector3:
    def test_button_PersonalAccount(self, driver, auth): 
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 10)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_button_constructor_in_PersonalAccount(self, driver, auth): 
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_button_logo(self, driver, auth): 
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 10)
        driver.find_element(By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a").click()
        WebDriverWait(driver, 10)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_button_loginExit_in_PersonalAccount(self, driver, auth): 
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 10)
        driver.find_element(By.CSS_SELECTOR, "button.Account_button__14Yp3").click()
        WebDriverWait(driver, 10)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
