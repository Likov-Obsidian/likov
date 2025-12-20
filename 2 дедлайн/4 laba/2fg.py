numbers = [45, 78, 23, 91, 34, 67, 12, 89, 56, 3]

even_numbers = []
for num in numbers:
    if num % 2 == 0: 
        even_numbers.append(num)
big_numbers = []
for num in numbers:
    if num > 50:
        big_numbers.append(num)

print("Исходный список чисел:", numbers)
print("Четные числа:", even_numbers)
print("Числа больше 50:", big_numbers)