fruits = {
    "яблок": 5,
    "бананов": 3,
    "апельсинов": 10,
    "арбузов": 33
}

print("Начальное количество:")
for fruit, count in fruits.items():
    print(f"за прилавком есть {count} {fruit}")
fruits["яблок"] = fruits["яблок"] - 2
print(f"\nПродали 2 яблока. Осталось {fruits['яблок']} яблок")
fruits["арбузов"] = 0
print("Ашот украл все арбузы!")
print("\nИтоговое количество:")
for fruit, count in fruits.items():
    print(f"за прилавком осталось {count} {fruit}")