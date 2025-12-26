def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * power(a, n - 1)
    else:
        return 1 / power(a, -n)
print(power(2, 3))
print(power(5, 0))
print(power(2, -2))