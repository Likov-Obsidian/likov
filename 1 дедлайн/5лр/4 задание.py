print("Введите 5 чисел:")
numbers = []
for i in range(5):
    num = float(input(f"Число {i+1}: "))
    numbers.append(num)
min_number = min(numbers)
max_number = max(numbers)
print(f"Минимальное число: {min_number}")
print(f"Максимальное число: {max_number}")