n = int(input("Сколько чисел ввести? "))
numbers = []
i = 0
while i < n:
    num = float(input(f"Введите число {i+1}: "))
    numbers.append(num)
    i += 1
maximum = numbers[0]
minimum = numbers[0]
summa = 0

i = 0
while i < n:
    if numbers[i] > maximum:
        maximum = numbers[i]
    if numbers[i] < minimum:
        minimum = numbers[i]
    summa += numbers[i]
    i += 1

average = summa / n
count_above = 0
i = 0
while i < n:
    if numbers[i] > average:
        count_above += 1
    i += 1
print(f"\nМаксимальное: {maximum}")
print(f"Минимальное: {minimum}")
print(f"Среднее арифметическое: {average}")
print(f"Чисел больше среднего: {count_above}")