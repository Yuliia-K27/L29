class HashTable:
    def __init__(self, size):
        # конструктор класу, створює хеш-таблицю заданої довжини
        self.size = size
        # ініціалізуємо список для бакетів, кожен бакет - порожній список
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # метод для визначення індексу бакета за ключем
        return key % self.size

    def add_element(self, key, value):
        # метод додає новий елемент до хеш-таблиці за допомогою ключа і значення
        index = self.hash_function(key)
        # перевірка, чи елемент з таким ключем вже існує в бакеті
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                # якщо так, то замінюємо його значення
                self.table[index][i] = (key, value)
                return
        # якщо елемент з таким ключем не існує, додаємо його до бакету
        self.table[index].append((key, value))

    def delete_element(self, key):
        # метод видаляє елемент з хеш-таблиці за допомогою ключа
        index = self.hash_function(key)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                # якщо елемент знайдено, видаляємо його з бакету
                del self.table[index][i]
                return

    def find_element(self, key):
        # метод повертає значення елемента за його ключем або None, якщо елемент не знайдено
        index = self.hash_function(key)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                # якщо елемент знайдено, повертаємо його значення
                return self.table[index][i][1]
        # якщо елемент не знайдено, повертаємо None
        return None

    def print_table(self):
        # метод друкує всі елементи хеш-таблиці
        for i in range(self.size):
            print(i, end=' ')
            for item in self.table[i]:
                print('-->', end=' ')
                print(item, end=' ')
            print()

    def resolve_collision(self):
        # метод вирішує колізії, тобто випадки, коли два елементи мають один і той самий індекс бакета
        for i in range(self.size):
            for j in range(len(self.table[i])):
                key = self.table[i][j][0]
                value = self.table[i][j][1]
                index = self.hash_function(key)
                # якщо елемент не знаходиться в правильному бакеті, переносимо його
                if index != i:
                    self.table[i].pop(j)
                    self.table[index].append((key, value))
