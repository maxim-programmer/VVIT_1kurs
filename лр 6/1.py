class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self._password = password
    def set_password(self, new_password):
        self._password = new_password
        print('Пароль изменён.')
    def check_password(self, password):
        return self._password == password

user = UserAccount('user123', 'example@mail.ru', 'old_password')

print(user.check_password(input('Введите ваш пароль: ')))
user.set_password(input('Введите ваш новый пароль: '))
print(user.check_password(input('Введите ваш пароль: ')))


