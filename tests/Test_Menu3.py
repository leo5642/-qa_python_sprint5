from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
#Переход в личный кабинет 

class TestBooksCollector3:
    def test_button_PersonalAccount(self): 
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login') 
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input").send_keys('lev_struin@mail.ru')
        driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input").send_keys('123123')
        driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0").click()
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quit() 

    def test_button_constructor_in_PersonalAccount(self): 
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login') 
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input").send_keys('lev_struin@mail.ru')
        driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input").send_keys('123123')
        driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0").click()
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit() 

    def test_button_logo(self): 
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login') 
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input").send_keys('lev_struin@mail.ru')
        driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input").send_keys('123123')
        driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0").click()
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 10)
        driver.find_element(By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a").click()
        WebDriverWait(driver, 10)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit() 


    def test_button_loginExit_in_PersonalAccount(self): 
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login') 
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input").send_keys('lev_struin@mail.ru')
        driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input").send_keys('123123')
        driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0").click()
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "button.Account_button__14Yp3").click()
        time.sleep(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()
