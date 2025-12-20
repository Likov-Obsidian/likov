def build_user_profile(user_id: int, **kwargs) -> dict:
    profile = {"user_id": user_id}
    profile.update(kwargs)
    return profile

print("Примеры создания профилей:")
print("=" * 40)
profile1 = build_user_profile(101, name="Арсений")
print(f"1. Простой профиль: {profile1}")

profile2 = build_user_profile(102, name="Иван", age=25, city="Нижневартовск")
print(f"2. Расширенный профиль: {profile2}")
profile3 = build_user_profile(103)
print(f"3. Только ID: {profile3}")
profile4 = build_user_profile(
    104, 
    name="Мария", 
    skills=["Python", "JavaScript"], 
    is_active=True,
    last_login="16-12-2025"
)
print(f"4. Разные типы данных: {profile4}")