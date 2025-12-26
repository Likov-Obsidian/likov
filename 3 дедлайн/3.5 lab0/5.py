import sys

#Создание списка
def create_list(n):
    return [i ** 2 for i in range(n)]

#Создание генератора
def create_gen(n):
    return (i ** 2 for i in range(n))

n = 1000000

lst = create_list(n)
gen = create_gen(n)

print(f"Размер списка: {sys.getsizeof(lst)} байт")
print(f"Размер генератора: {sys.getsizeof(gen)} байт")

print("\nСложность по памяти:")
print("- Список: O(n) - хранит все элементы")
print("- Генератор: O(1) - хранит только состояние")