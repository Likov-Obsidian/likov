print("Введите три целых числа через пробел")
user_input = input("Введите три числа: ")
numbers = user_input.split()
if len(numbers) != 3:
    print("Нужно ввести ровно 3 числа через пробел")
else:
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    num3 = int(numbers[2])
    print(f"\nВведенные числа: {num1}, {num2}, {num3}")
    mult1 = num1 * num2
    mult2 = num2 * num3
    mult3 = num3 * num1
    power4 = num1 ** 4
    remainder = num2 % num3
    int_division = num3 // num1
    print(f"Первое число * второе = {num1} * {num2} = {mult1}")
    print(f"Второе число * третье = {num2} * {num3} = {mult2}")
    print(f"Третье число * первое = {num3} * {num1} = {mult3}")
    print(f"Первое число в 4 степени = {num1} ** 4 = {power4}")
    print(f"Остаток от деления второго на третье = {num2} % {num3} = {remainder}")
    print(f"Целочисленное деление третьего на первое = {num3} // {num1} = {int_division}")
    sum_results = power4 + remainder + int_division
    print(f"Сумма ({power4} + {remainder} + {int_division}) = {sum_results}")