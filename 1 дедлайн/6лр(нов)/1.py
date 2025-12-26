fio = input("Введите ФИО через пробел: ")
formatted_fio = ' '.join(part.capitalize() for part in fio.split())
print(f"Добро пожаловать, {formatted_fio}")