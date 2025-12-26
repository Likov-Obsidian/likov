import time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
def tail_fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return tail_fibonacci(n - 1, b, a + b)
n = 35

print("=" * 50)
print(f"Вычисление Fibonacci({n})")
print("=" * 50)
start_time = time.time()
result1 = fibonacci(n)
time1 = time.time() - start_time
print(f"Fibonacci({n}) = {result1}")
print(f"Время обычной рекурсии: {time1:.6f} секунд")

print("-" * 50)
start_time = time.time()
result2 = tail_fibonacci(n)
time2 = time.time() - start_time
print(f"Tail Fibonacci({n}) = {result2}")
print(f"Время хвостовой рекурсии: {time2:.6f} секунд")

print("-" * 50)

print("Оба метода дали одинаковый результат:", result1 == result2)
print(f"Хвостовая рекурсия быстрее в {time1/time2:.2f} раз")