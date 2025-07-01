from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Profilepagelocators
#Переход в личный кабинет 

class Testbookscollector3:
    def test_button_persona_laccount(self, driver, auth): 
        profile_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Profilepagelocators.profile_button))
        profile_button.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_button_constructor_in_persona_laccount(self, driver, auth): 
        driver.find_element(*Profilepagelocators.profile_button).click()
        driver.find_element(*Profilepagelocators.kons_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_button_logo(self, driver, auth): 
        driver.find_element(*Profilepagelocators.profile_button).click()
        driver.find_element(*Profilepagelocators.logo_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_button_loginexit_in_persona_laccount(self, driver, auth): 
        driver.find_element(*Profilepagelocators.profile_button).click()
        acco_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Profilepagelocators.acco_button))
        acco_button.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'