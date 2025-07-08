from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import ProfilePageLocators
#Переход в личный кабинет 

class TestBooksCollector3:
    def test_button_persona_laccount(self, driver, auth): 
        profile_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ProfilePageLocators.profile_button))
        profile_button.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_button_constructor_in_persona_laccount(self, driver, auth): 
        driver.find_element(*ProfilePageLocators.profile_button).click()
        driver.find_element(*ProfilePageLocators.constructor_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_button_logo(self, driver, auth): 
        driver.find_element(*ProfilePageLocators.profile_button).click()
        driver.find_element(*ProfilePageLocators.logo_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_button_loginexit_in_persona_laccount(self, driver, auth): 
        driver.find_element(*ProfilePageLocators.profile_button).click()
        exit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ProfilePageLocators.exit_button))
        exit_button.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
