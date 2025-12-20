def display_user_profile(name, age, city):
    print("=" * 30)
    print("=" * 30)
    print(f"Имя:   {name}")
    print(f"Возраст: {age} лет")
    print(f"Город: {city}")
    print("=" * 30)

print("Пример 1 (обычный вызов):")
display_user_profile("Анна", 25, "стрежевой")
print("\nПример 2 (аргументы не по порядку):")
display_user_profile(city="нижневартовск", age=30, name="Яковенко")

print("\nПример 3 (еще один вариант):")
display_user_profile(age=22, name="Мария", city="Мегион")
user_name = input("Введите имя: ")
user_age = input("Введите возраст: ")
user_city = input("Введите город: ")
display_user_profile(
    city=user_city,
    name=user_name,
    age=user_age
)