def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
#primer777:
for num in fibonacci(6):
    print(num)