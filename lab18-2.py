import json
employees = {
    "Іванов": 12,
    "Петров": 18,
    "Сидоров": 20,
    "Коваленко": 15,
    "Ткаченко": 19,
    "Мельник": 21,
    "Шевченко": 25,
    "Гриценко": 22,
    "Бойко": 14,
    "Довженко": 23,
}
with open("employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, ensure_ascii=False)
print("Словник збережено у файл employees.json.")
with open("employees.json", "r", encoding="utf-8") as file:
    loaded_employees = json.load(file)
top_employees = {name: hours for name, hours in loaded_employees.items() if hours > 20}
print("Працівники, які відпрацювали більше 20 годин:")
for name, hours in top_employees.items():
    print(f"{name}: {hours} год.")