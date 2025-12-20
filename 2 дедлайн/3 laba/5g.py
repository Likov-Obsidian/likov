word_stats = {}

print("Введите текст (пустая строка для завершения):")

while True:
    line = input()
    
    if line == "":
        break
    
    words = line.split()
    
    for word in words:
        clean_word = word.strip('.,!?;:()"\'').lower()
        
        if clean_word:
            if clean_word in word_stats:
                word_stats[clean_word] += 1
            else:
                word_stats[clean_word] = 1

print("\nСтатистика слов:")
for word, count in word_stats.items():
    print(f"'{word}': {count}")