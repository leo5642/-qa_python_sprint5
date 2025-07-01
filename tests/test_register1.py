import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Authpagelocators
from data import Userdata
import random


class TestRegistration:
    def test_register_new_name_email_passowrld_random(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register') 

        user = Userdata()
        name = 'user' + str(random.randint(100, 99999))
        email = user.new_email
        passowrld = user.new_password

        driver.find_element(*Authpagelocators.login_input).send_keys(name)
        driver.find_element(*Authpagelocators.email_input).send_keys(email)
        driver.find_element(*Authpagelocators.password_input).send_keys(passowrld)
        driver.find_element(*Authpagelocators.login_button).click()
        
        WebDriverWait(driver, 10).until(
            ec.url_contains("https://stellarburgers.nomoreparties.site/login")
        )

    def test_error_passworld(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register') 

        driver.find_element(*Authpagelocators.password_input).send_keys('21312')
        driver.find_element(*Authpagelocators.login_button).click()
        
        error = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Authpagelocators.error_message)
        )
        assert error.text == 'Некорректный пароль'