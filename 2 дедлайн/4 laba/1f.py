grades = []
grades.append(4)
grades.append(5)
grades.append(3)
grades.append(4)
grades.append(2)
print("Текущие оценки:", grades)
grades.pop(0)
average_grade = sum(grades) / len(grades)
print(f"Средний балл: {average_grade:.2f}")

print("Итоговые оценки:", grades)