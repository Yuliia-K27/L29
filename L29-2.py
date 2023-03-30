import hashlib  # імпорт модуля для хешування паролів

# словник для зберігання пар "логін-пароль"
user_data = {}


# Функція реєстрації користувача
def register():
    print("***** РЕЄСТРАЦІЯ КОРИСТУВАЧА *****")
    login = input("Введіть логін: ")

    # перевірка чи вже є користувач з таким логіном
    if login in user_data:
        print("Користувач з таким логіном вже існує!")
        return
    
    # перевірка колізій
    if hashed_password in user_data.values():
        print("Цей пароль вже використовується!")
        return

    # запит пароля і його хешування за допомогою SHA-256
    password = input("Введіть пароль: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # збереження пари "логін-хеш пароля" в словнику
    user_data[login] = hashed_password
    print("Користувач зареєстрований успішно!")


# Функція авторизації користувача
def login():
    print("***** АВТОРИЗАЦІЯ КОРИСТУВАЧА *****")
    login = input("Введіть логін: ")

    # перевірка чи існує користувач з таким логіном
    if login not in user_data:
        print("Користувач з таким логіном не зареєстрований!")
        return

    # запит пароля і перевірка його правильності
    password = input("Введіть пароль: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if hashed_password == user_data[login]:
        print("Вхід виконано успішно!")
    else:
        print("Неправильний пароль!")


# виклик функцій реєстрації та авторизації користувача
register()
login()
