
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
#Конструктор

class TestBooksCollector4:
    def test_button_constructor_coys(self): 
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login') 
        WebDriverWait(driver, 10)

        driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input").send_keys('lev_struin@mail.ru')
        driver.find_element(By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input").send_keys('123123')
        driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0").click()
        WebDriverWait(driver, 10)

        time.sleep(5)
        driver.find_element(By.XPATH, "//div/span[text()='Соусы']").click()
        rd = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current__')]/span[@class='text text_type_main-default']")
        assert rd.text == 'Соусы'

        time.sleep(5)
        driver.find_element(By.XPATH, "//div/span[text()='Начинки']").click()
        rd = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current__')]/span[@class='text text_type_main-default']")
        assert rd.text == 'Начинки'

        time.sleep(5)
        driver.find_element(By.XPATH, "//div/span[text()='Булки']").click()
        rd = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current__')]/span[@class='text text_type_main-default']")
        assert rd.text == 'Булки'

        driver.quit()

