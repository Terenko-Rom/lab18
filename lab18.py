import pickle

# Генерація геометричної прогресії
def generate_geometric_progression(b1, q, n):
    progression = [b1 * (q ** i) for i in range(n)]
    return progression

# Запит у користувача кількості елементів
n = int(input("Введіть кількість елементів геометричної прогресії: "))
b1 = 2.5
q = 1.9

# Генерація списку
progression = generate_geometric_progression(b1, q, n)
print("Початковий список:", progression)

# Видалення перших 3 і останніх 3 елементів
trimmed_progression = progression[3:-3]

# Збереження у файл
with open("list.bin", "wb") as file:
    pickle.dump(trimmed_progression, file)

print("Список збережено у файл list.bin.")

# Зчитування з файлу та виведення
with open("list.bin", "rb") as file:
    loaded_progression = pickle.load(file)

print("Список із файлу:", loaded_progression)