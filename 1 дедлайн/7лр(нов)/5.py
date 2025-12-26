print("Введите выражение число1 операция число2")
user_input = input("Ваше выражение: ")
try:
    parts = user_input.split()
    if len(parts) != 3:
        print("Введите ровно три элемента через пробел.")
    else:
        num1 = float(parts[0])
        operation = parts[1]
        num2 = float(parts[2])
        result = None
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("деление на ноль нельзя")
        else:
            print(f"такой оерации нет'{operation}'")
        if result is not None:
            print(f"Результат: {num1} {operation} {num2} = {result}")
except ValueError:
    print("Числа некорректно ввели")