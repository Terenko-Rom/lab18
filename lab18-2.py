import shelve
employees = {
    "Іваненко": 18,
    "Петренко": 21,
    "Сидоренко": 19,
    "Коваленко": 22,
    "Шевченко": 20
}
with shelve.open("employees.db") as db:
    db["employees"] = employees
with shelve.open("employees.db") as db:
    saved_employees = db["employees"]
    print("Працівники, які відпрацювали більше 20 годин:")
    for name, hours in saved_employees.items():
        if hours > 20:
            print(f"{name}: {hours} годин")