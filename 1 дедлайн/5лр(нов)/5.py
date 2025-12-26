import random
import string
message = input("Введите сообщение: ")
n = int(input("Сколько случайных букв добавлять к каждой букве? "))
encoded = ""
for char in message:
    encoded += char
    for _ in range(n):
        random_letter = random.choice(string.ascii_letters)
        encoded += random_letter
print("\nЗакодированное послание:")
print(encoded)