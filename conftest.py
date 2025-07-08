import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import AuthData
from locators import AuthPageLocators

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def auth(driver):
    
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*AuthPageLocators.email_input).send_keys(AuthData.valid_email)
    driver.find_element(*AuthPageLocators.password_input).send_keys(AuthData.valid_password)
    driver.find_element(*AuthPageLocators.login_button).click()
