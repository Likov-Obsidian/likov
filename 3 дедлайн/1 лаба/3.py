def logger(func):

    def wrapper(*args, **kwargs):
        args_str = ", ".join([repr(arg) for arg in args])
        kwargs_str = ", ".join([f"{key}={repr(value)}" for key, value in kwargs.items()])
        
        all_args = []
        if args_str:
            all_args.append(args_str)
        if kwargs_str:
            all_args.append(kwargs_str)
        
        arguments = ", ".join(all_args)
        
        print(f"Вызов функции {func.__name__} с аргументами: ({arguments})")
        
        result = func(*args, **kwargs)
        
        print(f"Результат: {repr(result)}")
        print("-" * 50)
        
        return result
    
    return wrapper

@logger
def add_numbers(a, b):
    return a + b

@logger
def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"

@logger
def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

@logger
def create_user(name, age, city):
    return f"Пользователь: {name}, возраст: {age}, город: {city}"

print("тест")

print("\n1. Функция add_numbers:")
result1 = add_numbers(5, 3)
print(f"Итоговый результат: {result1}")

print("\n2. Функция greet:")
result2 = greet("Арсений", greeting="Добрый день")
print(f"Итоговый результат: {result2}")

print("\n3. Функция multiply:")
result3 = multiply(2, 3, 4, 5)
print(f"Итоговый результат: {result3}")

print("\n4. Функция create_user:")
result4 = create_user(name="Яковенко", age=25, city="Нижневартовск")
print(f"Итоговый результат: {result4}")

@logger
def get_current_time():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

print("\n5. Функция без аргументов:")
result5 = get_current_time()
print(f"Итоговый результат: {result5}")