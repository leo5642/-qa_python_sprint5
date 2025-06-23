
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
#Вход


class TestBooksCollector2:
    def test_button_ExitInLogin(self): 
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site') 
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit() 

    def test_button_PersonalAccount(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site') 
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_button_Exit_in_register(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register') 
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit() 

    def test_button_exit_in_password_recovery(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password') 
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit() 
