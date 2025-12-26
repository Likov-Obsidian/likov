text = input("Введите текст: ")
print(f"Текст: '{text}'")
print(f"Длина: {len(text)} символов")
start_user, end_user = map(int, input("Введите начало и конец диапазона: ").split())
start_py = start_user - 1
end_py = end_user
if start_py >= 0 and end_py <= len(text) and start_py < end_py:
    substring = text[start_py:end_py]
    print(f"\nПодстрока с {start_user} по {end_user} символ:")
    print(substring)
else:
    print("Некорректный диапазон")