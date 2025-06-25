import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def auth(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    
    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)
    )
    email_field.send_keys('lev_struin@mail.ru')
    
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AuthPageLocators.PASSWORD_INPUT)
    )
    password_field.send_keys('123123')
    
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(AuthPageLocators.LOGIN_BUTTON)
    )
    login_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.url_contains("https://stellarburgers.nomoreparties.site/")
    )
