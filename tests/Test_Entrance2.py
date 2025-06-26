from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#Вход


class Testbookscollector2:
    def test_button_exitInLogin(self, driver): 
        driver.get('https://stellarburgers.nomoreparties.site') 

        driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_button_personaaccount(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site') 

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_button_exit_in_register(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register') 

        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_button_exit_in_password_recovery(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password') 

        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
