password = input("Придумайте пароль: ")
confirm_password = input("Подтвердите пароль: ")
if password == confirm_password:
    print("Пароль установлен\n")
    login_password = input("Введите пароль: ")
    if login_password == password:
        print("Access")
    else:
        print("Denied")
else:
    print("Пароли не совпадают")