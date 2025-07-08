from selenium.webdriver.common.by import By


class AuthPageLocators:
    login_input =  (By.XPATH,"//label[contains(text(),'Имя')]/following-sibling::input")
    email_input = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    password_input = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    login_button = (By.CSS_SELECTOR, "button.button_button__33qZ0")
    error_message = (By.CLASS_NAME, 'input__error')



class ProfilePageLocators:
    of_zakas_button = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    profile_button = (By.XPATH, "//p[text()='Личный Кабинет']")
    exit_button_profile = (By.XPATH, ".//a[text()='Войти']")
    profile_header = (By.XPATH, "//h2[contains(text(),'Профиль')]")
    name_input = (By.XPATH, "//input[@name='name']")

    fillings_button = (By.XPATH, "//div/span[text()='Начинки']")
    button_active = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__')]/span[@class='text text_type_main-default']")
    sauce_button = (By.XPATH, "//div/span[text()='Соусы']")
    bread_button = (By.XPATH, "//div/span[text()='Булки']")

    constructor_button = (By.XPATH, ".//p[text()='Конструктор']")
    logo_button = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a")
    exit_button = (By.XPATH, ".//button[text()='Выход']")