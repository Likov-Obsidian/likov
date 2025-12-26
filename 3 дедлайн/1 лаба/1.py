def create_counter(start=0):

    count = start
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

print("счетчики с разными значениями")

counter1 = create_counter()
print("Счетчик 1 (старт с 0):")
print(f"Значение: {counter1()}")
print(f"Значение: {counter1()}")

counter2 = create_counter(10)
print("\nСчетчик 2 (старт с 10):")
print(f"Значение: {counter2()}")
print(f"Значение: {counter2()}")
counter3 = create_counter(-5)
print("\nСчетчик 3 (старт с -5):")
print(f"Значение: {counter3()}")
print(f"Значение: {counter3()}")