math = {"алиса", "ваня", "арсений", "яковенко"}
physics = {"игнат", "яковенко", "саша", "дима"}
cs = {"арсений", "игорь", "саша", "антон"}


print("\n1. Студенты на всех трех курсах:")
all_courses = math.intersection(physics, cs)
if all_courses:
    for student in all_courses:
        print(f"   {student}")
else:
    print("   (нет таких студентов)")

print("\n2. Студенты только на одном курсе:")

all_students = math | physics | cs

for student in sorted(all_students):
    count = 0
    if student in math: count += 1
    if student in physics: count += 1
    if student in cs: count += 1
    
    if count == 1:
        if student in math: course = "математике"
        elif student in physics: course = "физике"
        else: course = "информатике"
        print(f"   {student} (только на {course})")

print("\n3. Студенты на математике, но не на физике:")
math_only = math - physics
if math_only:
    for student in sorted(math_only):
        print(f"   {student}")
else:
    print("   (нет таких студентов)")

print(f"\n4. Всего уникальных студентов: {len(all_students)}")
print("   Список:", ", ".join(sorted(all_students)))