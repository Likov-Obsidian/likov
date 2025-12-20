def find_max(a, b):
    if a > b:
        return a
    else:
        return b
def find_max_simple(a, b):
    return a if a > b else b
print(find_max(5, 10))
print(find_max(-3, 0))
print(find_max(7, 7))

x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
maximum = find_max(x, y)
print(f"Большее число: {maximum}")