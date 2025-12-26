print("Введите 5 чисел:")
num1 = float(input("Число 1: "))
minimum = num1
maximum = num1
for i in range(2, 6):
    num = float(input(f"Число {i}: "))
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num
print(f"\nМинимальное число: {minimum}")
print(f"Максимальное число: {maximum}")