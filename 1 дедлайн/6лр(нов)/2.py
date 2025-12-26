text = input("Введите текст: ")
str1, str2 = input("Что заменить и на что (через пробел): ").split()
print("\nРезультат:", text.replace(str1, str2))