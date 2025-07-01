import random

class Authdata:
    valid_email = "lev_struin@mail.ru"
    valid_password = "123123"
    invalid_password = "123"

class Userdata:
    name = "Тестовый Пользователь"
    
    @property
    def new_email(self):
        return f"test{random.randint(100, 999)}@test.ru"
    
    @property
    def new_password(self):
        return str(random.randint(100000, 999999))