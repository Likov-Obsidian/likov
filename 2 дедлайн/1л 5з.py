text = input("Введите строку: ")
result = ""
i = 0

vowels = "аеёиоуыэюяaeiouy"

while i < len(text):
    if text[i].lower() not in vowels:
        result += text[i]
    i += 1

print(result)