import shelve

# Користувач задає кількість елементів прогресії
N = int(input("Введіть кількість елементів геометричної прогресії: "))
b1 = 2.5
q = 1.9

# Генеруємо геометричну прогресію
progression = [b1 * (q ** i) for i in range(N)]

# Видаляємо перші 3 і останні 3 елементи
if len(progression) > 6:
    trimmed_list = progression[3:-3]
else:
    trimmed_list = []

# Збереження списку в файл
with shelve.open("list.bin") as db:
    db["progression"] = trimmed_list

# Читання списку з файлу і його виведення
with shelve.open("list.bin") as db:
    saved_list = db["progression"]
    print("Список із файлу:", saved_list)
