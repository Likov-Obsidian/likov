text = input("Введи текст: ")
numbers = input("Введи диапазон (например: 3 6): ")
start, end = numbers.split()
start = int(start)
end = int(end)
result = text[start:end]
print("Результат:", result)