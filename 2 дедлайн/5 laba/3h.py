colors = {
    "красный": (255, 0, 0),
    "зеленый": (0, 255, 0),
    "синий": (0, 0, 255),
    "желтый": (255, 255, 0),
    "фиолетовый": (128, 0, 128),
    "белый": (255, 255, 255),
    "черный": (0, 0, 0)
}

print("словарь цветов")
for color in colors:
    print(f"{color}: {colors[color]}")

print("\nсмешивание цветов")

color1_name = "красный"
color2_name = "синий"

color1 = colors[color1_name]
color2 = colors[color2_name]

mixed_r = (color1[0] + color2[0]) // 2
mixed_g = (color1[1] + color2[1]) // 2
mixed_b = (color1[2] + color2[2]) // 2

mixed_color = (mixed_r, mixed_g, mixed_b)
print(f"Смешиваем {color1_name} {color1} и {color2_name} {color2}")
print(f"Получаем: {mixed_color}")

print("\nинвентирование цвета")

color_to_invert = "белый"
original_color = colors[color_to_invert]

inverted_r = 255 - original_color[0]
inverted_g = 255 - original_color[1]
inverted_b = 255 - original_color[2]

inverted_color = (inverted_r, inverted_g, inverted_b)
print(f"Инвертируем {color_to_invert} {original_color}")
print(f"Получаем: {inverted_color}")

print("\nпроверка")
if inverted_color == colors["черный"]:
    print("Инвертированный белый это черный")
else:
    print("Что-то пошло не так")