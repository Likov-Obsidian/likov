try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    sum_result = num1 + num2
    diff_result = num1 - num2
    mult_result = num1 * num2
    div_result = num1 / num2 if num2 != 0 else "Ошибка: деление на ноль!"
    print(f"Сложение: {num1} + {num2} = {sum_result}")
    print(f"Вычитание: {num1} - {num2} = {diff_result}")
    print(f"Умножение: {num1} × {num2} = {mult_result}")
    print(f"Деление: {num1} ÷ {num2} = {div_result}")
except ValueError:
    print("Ошибка! Введите корректные числа.")