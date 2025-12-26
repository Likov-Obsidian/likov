fio = input("Введите ФИО через пробел: ").split()
if len(fio) >= 3:
    print("\nФамилия:", fio[0].upper())
    print("Имя:", fio[1].upper())
    print("Отчество:", fio[2].upper())
else:
    print("Ошибка введите фамилию, имя и отчество")