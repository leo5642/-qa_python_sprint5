import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import AuthPageLocators
from data import UserData
import random


class TestBooksCollector1:
    def test_register_new_name_email_passowrld_random(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register') 

        user = UserData()
        name = 'user' + str(random.randint(100, 99999))
        email = user.new_email
        passowrld = user.new_password

        driver.find_element(*AuthPageLocators.login_input).send_keys(name)
        driver.find_element(*AuthPageLocators.email_input).send_keys(email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(passowrld)
        driver.find_element(*AuthPageLocators.login_button).click()
        
        WebDriverWait(driver, 10).until(
            ec.url_contains("https://stellarburgers.nomoreparties.site/login")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_error_passworld(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register') 

        driver.find_element(*AuthPageLocators.password_input).send_keys('21312')
        driver.find_element(*AuthPageLocators.login_button).click()
        
        error = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(AuthPageLocators.error_message)
        )
        assert error.text == 'Некорректный пароль'
