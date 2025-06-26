from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random

class Testbookscollector1:
    def test_register_new_name_email_passowrld_random(self, driver): 
        driver.get('https://stellarburgers.nomoreparties.site/register') 

        name = 'user' + str(random.randint(100, 99999))
        email = name + '@test.ru' 
        passowrld = random.randint(100000, 99999999)

        driver.find_element(By.XPATH,"//label[contains(text(),'Имя')]/following-sibling::input").send_keys(name)
        driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input").send_keys(email)
        driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input").send_keys(passowrld)
        driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'



    def test_error_passworld(self, driver): 
        driver.get('https://stellarburgers.nomoreparties.site/register') 

        driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input").send_keys('21312')
        driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0").click()
        assert 'Некорректный пароль' == driver.find_element(By.CLASS_NAME, 'input__error').text
