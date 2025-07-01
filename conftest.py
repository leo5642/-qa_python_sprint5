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
    driver.find_element(*Authpagelocators.email_input).send_keys(Authdata.valid_email)
    driver.find_element(*Authpagelocators.password_input).send_keys(Authdata.valid_password)
    driver.find_element(*Authpagelocators.login_button).click()
