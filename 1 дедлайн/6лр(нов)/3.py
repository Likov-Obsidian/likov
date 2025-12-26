text = input("Введите текст: ")
try:
    step = int(input("Введите шаг: "))
    result = text[::step]
    print("\nТекст с заданным шагом: ")
    print(result)
except ValueError:
    print("Ошибка, введите целое число для шага")