phone_book = {
    "Арсений": "123-456",
    "Яковенко": "789-012"
}

while True:
    print("\nТелефонная книга")
    print("1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("3 - Удалить контакт")
    print("4 - Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        print("\nВсе контакты:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    
    elif choice == "2":
        name = input("Введите имя: ")
        if name in phone_book:
            print("Контакт с таким именем уже существует!")
        else:
            phone = input("Введите телефон: ")
            phone_book[name] = phone
            print(f"Контакт {name} добавлен!")
    

    elif choice == "3":
        name = input("Введите имя для удаления: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Контакт {name} удален!")
        else:
            print("Контакт не найден!")
    elif choice == "4":
        print("До свидания!")
        exit()
    
    else:
        print("Неверный выбор!")