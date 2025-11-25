import math

user_input = input("Введите выражение (например: 5 + 3): ")

parts = user_input.split()

print ("num1 = float(parts[0])/n operator = parts[1]/n num2 = float(parts[2])")
    
if operator == "+":
        result = num1 + num2
elif operator == "-":
        result = num1 - num2
elif operator == "*":
        result = num1 * num2
elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Ошибка: деление на ноль!"
elif operator == "%":
        result = num1 % num2
elif operator == "//":
        if num2 != 0:
            result = num1 // num2
        else:
            result = "Ошибка: деление на ноль!"
elif operator == "**":
        result = num1 ** num2
elif operator == "%%":
        result = (num2 / 100) * num1
elif operator == "/**":
        if num1 >= 0:
            result = math.sqrt(num1)
        else:
            result = "Ошибка: корень из отрицательного числа!"
else:
        result = "Ошибка: неизвестная операция!"
    
    # Выводим результат
print(f"Результат: {result}")