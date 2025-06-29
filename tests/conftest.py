import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_data import AuthData
import random
from locators import AuthPageLocators


class Authdata:
    valid_email = "lev_struin@mail.ru"
    valid_password = "123123"
    invalid_password = "123"

class Userdata:
    name = "Тестовый Пользователь"
    new_email = f"test{random.randint(100, 999)}@test.ru"
    new_password = str(random.randint(100000, 999999))

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


class Authpagelocators:
    login_input =  (By.XPATH,"//label[contains(text(),'Имя')]/following-sibling::input")
    email_input = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    password_input = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    login_button = (By.CSS_SELECTOR, "button.button_button__33qZ0")
    error_message = (By.CLASS_NAME, 'input__error')
class Profilepagelocators:
    of_zakas_button = (By.XPATH, ".//button[text()='Оформить заказ']")
    profile_button = (By.XPATH, "//p[text()='Личный Кабинет']")
    exit_button = (By.XPATH, ".//a[text()='Войти']")
    profile_header = (By.XPATH, "//h2[contains(text(),'Профиль')]")
    name_input = (By.XPATH, "//input[@name='name']")

    nach_button = (By.XPATH, "//div/span[text()='Начинки']")
    vibor_button = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__')]/span[@class='text text_type_main-default']")
    coyc_button = (By.XPATH, "//div/span[text()='Соусы']")
    bylk_button = (By.XPATH, "//div/span[text()='Булки']")

    kons_button = (By.XPATH, ".//p[text()='Конструктор']")
    logo_button = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a")
    acco_button = (By.CSS_SELECTOR, "button.Account_button__14Yp3")
