def simple_calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка деление на ноль"
    else:
        return "Ошибка неверный оператор"
print(simple_calculator(10, 5, '+'))
print(simple_calculator(10, 5, '-'))
print(simple_calculator(10, 5, '*'))
print(simple_calculator(10, 5, '/'))
print(simple_calculator(10, 0, '/'))
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Введите оператор (+, -, *, /): ")
result = simple_calculator(a, b, op)
print(f"{a} {op} {b} = {result}")