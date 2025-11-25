while True:
    direction = input("Введите направление (влево/вправо/прямо/назад): ").lower()
    
    if direction == "влево":
        print("Иду влево")
    elif direction == "вправо":
        print("Иду вправо")
    elif direction == "прямо":
        print("Иду прямо")
    elif direction == "назад":
        print("Иду назад")
    else:
        print("неправильное направление")