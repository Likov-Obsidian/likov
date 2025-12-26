def safe_exec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль")
            return 0
    return wrapper

@safe_exec
def divide(a, b):
    return a / b

print(f"Результат АДИН: {divide(10, 2)}")
print(f"Результат ДВА: {divide(5, 0)}")