text = input("Введите текст: ")
word = input("Введите слово для поиска: ")
count = text.count(word)
print("\nРезультат поиска:")
if word in text:
    print(f"Слово '{word}' есть в тексте")
    print(f"Количество вхождений: {count}")
else:
    print(f"Слова '{word}' нет в тексте")
    print("Количество вхождений: 0")