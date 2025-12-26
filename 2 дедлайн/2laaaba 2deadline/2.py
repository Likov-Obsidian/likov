n = int(input("Введите число: "))
print(f"Таблица умножения для числа {n}:")
print("=" * 20)
for i in range(1, 11):
    print(f"{i}")
    print(f"{n} * {i} = {n * i}")