print("Введите два числа:")
num1 = float(input("Первое число: "))
num2 = float(input("Второе число: "))
print("\nРезультаты вычислений:")
print(f"Сложение: {num1} + {num2} = {num1 + num2}")
print(f"Вычитание: {num1} - {num2} = {num1 - num2}")
print(f"Умножение: {num1} * {num2} = {num1 * num2}")
if num2 != 0:
    print(f"Деление: {num1} / {num2} = {num1 / num2}")
else:
    print("На ноль делить нельзя")