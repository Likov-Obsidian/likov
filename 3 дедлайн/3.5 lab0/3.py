import time
import random

def find_duplicates_slow(arr):
    #Поиск дубликатов с O(n²) - вложенные циклы
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                duplicates.append(arr[i])
                break
    return duplicates

def generate_random_list(size):
    #Генерация списка случайных чисел
    return [random.randint(1, 1000) for _ in range(size)]

def test_performance(size):
    #Тестирование производительности для заданного размера
    arr = generate_random_list(size)
    
    start_time = time.time()
    result = find_duplicates_slow(arr)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    return elapsed_time, len(result)

# Тестируем для разных размеров
print("Тестирование производительности O(n²) алгоритма:")
print("=" * 50)

# Первый тест: 5000 элементов
time1, duplicates1 = test_performance(5000)
print(f"Размер списка: 5000 элементов")
print(f"Время выполнения: {time1:.2f} секунд")
print(f"Найдено дубликатов: {duplicates1}")

print("\n" + "-" * 30)

# Второй тест: 10000 элементов
time2, duplicates2 = test_performance(10000)
print(f"Размер списка: 10000 элементов")
print(f"Время выполнения: {time2:.2f} секунд")
print(f"Найдено дубликатов: {duplicates2}")

print("\n" + "=" * 50)

# Вычисляем во сколько раз выросло время
if time1 > 0:
    growth_factor = time2 / time1
    print(f"\nВремя выполнения выросло в {growth_factor:.1f} раза")
    
    print(f"Теоретически для O(n²) при увеличении в 2 раза, время должно вырасти в 4 раза")
    print(f"На практике: {growth_factor:.1f} раз")

    if growth_factor > 3:
        print("\n✓ Результат близок к теоретическому O(n²): время выросло примерно в 4 раза")
    else:
        print("\n Результат отличается от теоретического из-за оптимизаций Python")
else:
    print("Время выполнения слишком мало для точного измерения")