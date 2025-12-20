def power(number, exponent=2):
    return number ** exponent

print(power(3))
print(power(2, 3))
print(power(5, 4))
print(power(10))

num = int(input("Введите число: "))
exp = input("Введите степень (нажмите Enter для квадрата): ")
if exp == "":
    result = power(num)
    print(f"{num}² = {result}")
else:
    result = power(num, int(exp))
    print(f"{num}^{exp} = {result}")