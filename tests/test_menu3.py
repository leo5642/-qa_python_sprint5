from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#Переход в личный кабинет 

class Testbookscollector3:
    def test_button_persona_laccount(self, driver, auth): 
        driver.find_element(*LoginPageLocators.profile_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_button_constructor_in_persona_laccount(self, driver, auth): 
        driver.find_element(*LoginPageLocators.profile_button).click()
        driver.find_element(*LoginPageLocators.kons_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_button_logo(self, driver, auth): 
        driver.find_element(*LoginPageLocators.profile_button).click()
        driver.find_element(*LoginPageLocators.logo_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_button_loginexit_in_persona_laccount(self, driver, auth): 
        driver.find_element(*LoginPageLocators.profile_button).click()
        driver.find_element(*LoginPageLocators.acco_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
