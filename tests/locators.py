from selenium.webdriver.common.by import By

class Authpagelocators:
    email_input = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    password_input = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")
    login_button = (By.CSS_SELECTOR, "button.button_button__33qZ0")

class Profilepagelocators:
    profile_button = (By.XPATH, "//p[text()='Личный Кабинет']")
    profile_header = (By.XPATH, "//h2[contains(text(),'Профиль')]")
    name_input = (By.XPATH, "//input[@name='name']")
