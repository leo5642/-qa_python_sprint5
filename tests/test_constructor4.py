from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import ProfilePageLocators
#Конструктор

class TestBooksCollector4:
    def test_button_constructor_sauce(self, driver, auth): 
        sauce_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ProfilePageLocators.sauce_button))
        sauce_button.click()
        active_button = driver.find_element(*ProfilePageLocators.button_active)
        assert active_button.text == 'Соусы'


    def test_button_construktor_fillings(self, driver, auth):
        fillings_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ProfilePageLocators.fillings_button))
        fillings_button.click()
        active_button = driver.find_element(*ProfilePageLocators.button_active)
        assert active_button.text == 'Начинки'


    def test_button_construktor_bread(self, driver, auth):
        sauce_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ProfilePageLocators.sauce_button))
        sauce_button.click()
        bread_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ProfilePageLocators.bread_button))
        bread_button.click()
        active_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(ProfilePageLocators.button_active))
        assert active_button.text == 'Булки'

