text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

count = text.lower().count(word.lower())

if count > 0:
    print(f"Слово '{word}' найдено в тексте. Количество раз: {count}")
else:
    print(f"Слово '{word}' не найдено в тексте.")