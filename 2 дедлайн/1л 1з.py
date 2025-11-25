number = int(input("Введите положительное целое число: "))
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10
print(f"Сумма цифр: {sum_of_digits}")