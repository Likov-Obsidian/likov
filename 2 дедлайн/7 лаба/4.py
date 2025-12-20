call_counter = 0

def increment_counter():
    global call_counter
    call_counter += 1
    print(f"Функция вызвана. Счетчик: {call_counter}")

print("Начальное значение счетчика:", call_counter)

increment_counter()
increment_counter()
increment_counter()

print("Итоговое значение счетчика:", call_counter)