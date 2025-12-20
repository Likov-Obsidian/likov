students = [
    ("Анна", 22, 4.5),
    ("Иван", 19, 3.8),
    ("Мария", 21, 4.9),
    ("Петр", 20, 4.2),
    ("Ольга", 18, 4.7)
]

print("Все студенты")
for name, age, score in students:
    print(f"{name} - {age} лет, средний балл: {score}")

print("\nСтуденты старше 20 лет")
count_over_20 = 0
for name, age, score in students:
    if age > 20:
        print(f"{name}, {age} лет")
        count_over_20 += 1
if count_over_20 == 0:
    print("Нет студентов старше 20 лет")

max_score = 0
best_student_name = ""
best_student_age = 0

for name, age, score in students:
    if score > max_score:
        max_score = score
        best_student_name = name
        best_student_age = age

print(f"\n Лучший студент")
print(f"{best_student_name}, {best_student_age} лет, балл: {max_score}")

print("\n Сортировка по имени")
names_only = []
for student in students:
    names_only.append(student[0])

names_only.sort()
for name in names_only:
    for student in students:
        if student[0] == name:
            print(f"{student[0]} - {student[1]} лет, балл: {student[2]}")
            break