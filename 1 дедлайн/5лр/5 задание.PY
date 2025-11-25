import random
import string

def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

message = input("Введи сообщение: ")
n = int(input("Введи количество подстановочных символов: "))
encoded_message = ""
for char in message:
    encoded_message += char
    encoded_message += generate_random_string(n)

print("\nЗакодированное сообщение:")
print(encoded_message)