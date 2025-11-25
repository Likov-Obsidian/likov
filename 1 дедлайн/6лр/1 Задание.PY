fio_input = input("Введите ваше ФИО через пробел: ")
parts = fio_input.split()
if len(parts) == 3:
    formatted_parts = [part.capitalize() for part in parts]
    formatted_fio = ' '.join(formatted_parts)
    print(f"Добро пожаловать, {formatted_fio}!")