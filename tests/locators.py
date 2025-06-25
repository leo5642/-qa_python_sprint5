from selenium.webdriver.common.by import By

class AuthPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0")

class ProfilePageLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    PROFILE_HEADER = (By.XPATH, "//h2[contains(text(),'Профиль')]")
