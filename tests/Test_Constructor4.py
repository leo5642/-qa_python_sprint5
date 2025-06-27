from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#Конструктор

class Testbookscollector4:
    def test_button_constructor_coys(self, driver, auth): 
        driver.find_element(*LoginPageLocators.coyc_button).click()
        rd = driver.find_element(*LoginPageLocators.vibor_button)
        assert rd.text == 'Соусы'


    def test_button_construktor_nachinki(self, driver, auth):

        driver.find_element(*LoginPageLocators.nach_button).click()
        rd = driver.find_element(*LoginPageLocators.vibor_button)
        assert rd.text == 'Начинки'


    def test_button_construktor_boolki(self, driver, auth):

        driver.find_element(*LoginPageLocators.coyc_button).click()
        driver.find_element(*LoginPageLocators.bylk_button).click()
        rd = driver.find_element(*LoginPageLocators.vibor_button)
        assert rd.text == 'Булки'

