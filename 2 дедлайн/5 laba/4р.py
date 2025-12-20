text = input("Введите текст: ")

if text == "":
    print("Текст не введен")
    exit()

print("\nанализ текста")

lower_text = text.lower()

clean_text = lower_text.replace(".", "").replace(",", "")
all_words = clean_text.split()

unique_words = set(all_words)

print(f"\nВсего слов: {len(all_words)}")
print(f"Уникальных слов: {len(unique_words)}")

print("\nСлова длиной более 5 символов:")
count_long = 0
for word in unique_words:
    if len(word) > 5:
        print(f"  {word}")
        count_long += 1

if count_long == 0:
    print("  (таких слов нет)")

print("\nПроверка ключевых слов:")
found_python = False
found_programming = False

for word in unique_words:
    if word == "python":
        found_python = True
    if word == "programming":
        found_programming = True

if found_python:
    print("+ Слово 'python' найдено")
else:
    print("- Слово 'python' не найдено")

if found_programming:
    print("+ Слово 'programming' найдено")
else:
    print("- Слово 'programming' не найдено")