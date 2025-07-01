import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import Authdata
from locators import Authpagelocators

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def auth(driver):
    
    driver.get('https://stellarburgers.nomoreparties.site/login')
    
    email_field = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(AuthPageLocators.email_input)
    )
    email_field.send_keys(AuthData.valid_email)
    
    password_field = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(AuthPageLocators.password_input)
    )
    password_field.send_keys(AuthData.valid_password)
    
    login_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(AuthPageLocators.login_button)
    )
    login_button.click()
    
    WebDriverWait(driver, 10).until(
        ec.url_contains("https://stellarburgers.nomoreparties.site/")
    )

