# імпорт модуля для хешування паролів
import hashlib  

class HashTable:
    def __init__(self, size=100):
        self.size = size
        # створюємо порожні списки для кожного індексу таблиці
        self.table = [[] for _ in range(size)] 
        
    def _hash(self, key):
        return int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % self.size
    
    # додавання елемента до хеш-таблиці
    def add(self, key, value):
        hashed_key = self._hash(key)
        for pair in self.table[hashed_key]:
            # перевірка чи існує вже елемент з таким ключем
            if pair[0] == key:
                pair[1] = value
                return
        # якщо елемент з таким ключем не знайдено, додаємо новий елемент
        self.table[hashed_key].append([key, value])

    # отримання елемента з хеш-таблиці по ключу
    def get(self, key):
        hashed_key = self._hash(key)
        for pair in self.table[hashed_key]:
            if pair[0] == key:
                return pair[1]
        # якщо елемент з таким ключем не знайдено, викидаємо виняток
        raise KeyError(key)

    # видалення елемента з хеш-таблиці по ключу
    def remove(self, key):
        hashed_key = self._hash(key)
        for i, pair in enumerate(self.table[hashed_key]):
            if pair[0] == key:
                del self.table[hashed_key][i]
                return
        # якщо елемент з таким ключем не знайдено, викидаємо виняток
        raise KeyError(key)

class User:
    def __init__(self, login, password):
        self.login = login
        self.password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

class AuthSystem:
    def __init__(self):
        self.users = HashTable()

    # реєстрація користувача з унікальним логіном та хешованим паролем
    def register_user(self):
        login = input("Enter login: ")
        password = input("Enter password: ")
        # первірка колізій
        if self.users.get(login):
            # перевірка на унікальність логіну
            print("User with such login already exists!")
            return
        user = User(login, password)
        self.users.add(user.login, user)
        print("User registered successfully!")

    def login(self):
        # авторизація користувача з логіном та паролем
        login = input("Enter login: ")
        password = input("Enter password: ")
        user = self.users.get(login)
        if user.password_hash == hashlib.sha256(password.encode('utf-8')).hexdigest():
            print("Authorized!")
        else:
            print("Wrong login or password.")
        
# виклик функцій реєстрації та авторизації користувача
auth_system = AuthSystem()
auth_system.register_user()
auth_system.login()

