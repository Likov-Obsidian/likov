print("регистрация лыков.ру")
password = input("Придумайте пароль: ")
confirm_password = input("Подтвердите пароль: ")

if password != confirm_password:
    print("Пароли не совпадают")
else:
    print("Пароль успешно установлен!\n")

    print("авторизация лыков.ру")
    login_password = input("Введите пароль: ")
    
    if login_password == password:
        print("Access")
    else:
        print("Denied")