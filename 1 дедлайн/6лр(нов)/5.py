text = input("Введите текст: ")
word = input("Введите слово для поиска: ")
count = text.count(word)
first_index = text.find(word)
print(f"\nРезультаты поиска слова '{word}':")
print(f"Количество встреч: {count}")
if first_index != -1:
    print(f"Индекс первого вхождения: {first_index}")
    print(f"Позиция для пользователя (с 1): {first_index + 1}")
else:
    print("Слово не найдено в тексте")
new_text = text.replace(word, "")
print(f"\nТекст без слова '{word}':")
print(new_text)