text = input("Введите строку: ")

cleaned_text = text.lower().replace(" ", "")

left = 0
right = len(cleaned_text) - 1
is_palindrome = True

while left < right:
    if cleaned_text[left] != cleaned_text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print(f"Строка '{text}' является палиндромом")
else:
    print(f"Строка '{text}' не является палиндромом")