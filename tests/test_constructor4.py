from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Profilepagelocators
#Конструктор

class Testbookscollector4:
    def test_button_constructor_coys(self, driver, auth): 
        coyc_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Profilepagelocators.coyc_button))
        coyc_button.click()
        rd = driver.find_element(*Profilepagelocators.vibor_button)
        assert rd.text == 'Соусы'


    def test_button_construktor_nachinki(self, driver, auth):
        nach_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Profilepagelocators.nach_button))
        nach_button.click()
        rd = driver.find_element(*Profilepagelocators.vibor_button)
        assert rd.text == 'Начинки'


    def test_button_construktor_boolki(self, driver, auth):
        coyc_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Profilepagelocators.coyc_button))
        coyc_button.click()
        bylk_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Profilepagelocators.bylk_button))
        bylk_button.click()
        rd = driver.find_element(*Profilepagelocators.vibor_button)
        assert rd.text == 'Булки'

