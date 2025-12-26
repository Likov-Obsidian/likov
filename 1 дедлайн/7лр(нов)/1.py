direction = input("Введите направление (left, right, straight, back): ").strip().lower()
if direction == "left":
    print("Иду влево")
elif direction == "right":
    print("Иду вправо")
elif direction == "straight":
    print("Иду прямо")
elif direction == "back":
    print("Иду назад")
else:
    print("Неправильное направление")