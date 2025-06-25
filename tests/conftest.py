import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    WebDriverWait(driver, 10)
    yield driver
    driver.quit()

@pytest.fixture
def auth(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input").send_keys('lev_struin@mail.ru')
    driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input").send_keys('123123')
    driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0").click()
    WebDriverWait(driver, 10)
