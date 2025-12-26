import time

#Удаление из начала списка (pop(0))
list1 = list(range(100_000))

start_time = time.time()
for _ in range(1000):
    list1.pop(0)
end_time = time.time()

time_pop_0 = end_time - start_time
print(f"Время для 1000 вызовов pop(0): {time_pop_0:.4f} секунд")

#Удаление с конца списка (pop())
list2 = list(range(100_000))

start_time = time.time()
for _ in range(1000):
    list2.pop()
end_time = time.time()

time_pop = end_time - start_time
print(f"Время для 1000 вызовов pop(): {time_pop:.4f} секунд")

# 3. Сравнение
print(f"\npop() быстрее pop(0) в {time_pop_0 / time_pop:.1f} раз")
