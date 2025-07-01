from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Profilepagelocators
#Вход


class Testbookscollector2:
    def test_button_exitin_login(self, driver): 
        driver.get('https://stellarburgers.nomoreparties.site') 

        driver.find_element(*Profilepagelocators.of_zakas_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_button_persona_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site') 

        driver.find_element(*Profilepagelocators.profile_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_button_exit_in_register(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register') 

        driver.find_element(*Profilepagelocators.exit_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_button_exit_in_password_recovery(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password') 

        driver.find_element(*Profilepagelocators.exit_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
