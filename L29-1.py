class HashTable:
    def __init__(self, size):               # конструктор класу, створює хеш-таблицю заданої довжини
        self.size = size
        # ініціалізуємо список для бакетів, кожен бакет - порожній список
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):             # метод для визначення індексу бакета за ключем
        return key % self.size

    def add_element(self, key, value):        # метод додає новий елемент до хеш-таблиці за допомогою ключа і значення
        index = self.hash_function(key)       # перевірка, чи елемент з таким ключем вже існує в бакеті
        for bucket_item in self.table[index]:
            if bucket_item[0] == key:          # якщо так, то замінюємо його значення
                bucket_item = (key, value)
                return
        self.table[index].append((key, value))  # якщо елемент з таким ключем не існує, додаємо його до бакету

    def delete_element(self, key):               # метод видаляє елемент з хеш-таблиці за допомогою ключа
        index = self.hash_function(key)
        for i, bucket_item in enumerate(self.table[index]):
            if bucket_item[0] == key:
                del self.table[index][i]            # якщо елемент знайдено, видаляємо його з бакету
                return

    def find_element(self, key):                    # метод повертає значення елемента за його ключем або None, якщо елемент не знайдено
        index = self.hash_function(key)
        for bucket_item in self.table[index]:
            if bucket_item[0] == key:
                return bucket_item[1]                # якщо елемент знайдено, повертаємо його значення
        return None                                   # якщо елемент не знайдено, повертаємо None

    def print_table(self):
        for i, bucket in enumerate(self.table):        # метод друкує всі елементи хеш-таблиці
            print(i, end=' ')
            for bucket_item in bucket:
                print('-->', end=' ')
                print(bucket_item, end=' ')
            print()

    def resolve_collision(self):
       for i, bucket in enumerate(self.table):           # метод вирішує колізії, тобто випадки, коли два елементи мають один і той самий індекс бакета
            for bucket_item in bucket:
                key = bucket_item[0]
                value = bucket_item[1]
                index = self.hash_function(key)
                if index != i:                                 # якщо елемент не знаходиться в правильному бакеті, переносимо його
                    self.table[index].append((key, value))     # додаємо елемент до правильного бакету
                    self.table[i].remove((key, value))         # видаляємо елемент зі старого бакету
                    
                    
                    
