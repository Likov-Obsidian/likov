text = input("Введите текст: ")
char_count = {}
for char in text.lower():
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("Результат подсчета:")
for char, count in char_count.items():
    print(f"'{char}': {count}")