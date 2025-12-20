def sum_numbers(*numbers: float) -> float:
    total = 0.0
    for num in numbers:
        total += num
    return total
print("Примеры работы функции:")
print(f"sum_numbers(1, 2, 3) = {sum_numbers(1, 2, 3)}")
print(f"sum_numbers(10, 20, 30, 40) = {sum_numbers(10, 20, 30, 40)}")
print(f"sum_numbers(1.5, 2.5, 3.5) = {sum_numbers(1.5, 2.5, 3.5)}")
print(f"sum_numbers() = {sum_numbers()}")
print(f"sum_numbers(100) = {sum_numbers(100)}")

print("\nваш вариант")
user_input = input("Введите числа через пробел: ")
if user_input:
    numbers_list = [float(x) for x in user_input.split()]
    result = sum_numbers(*numbers_list)
    print(f"Сумма чисел: {result}")
else:
    print("Вы не ввели числа. Сумма: 0")