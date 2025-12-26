n = int(input("Сколько чисел? "))
nums = [float(input(f"Число {i+1}: ")) for i in range(n)]
max_num = max(nums)
min_num = min(nums)
avg = sum(nums) / n
above = sum(1 for x in nums if x > avg)
print(f"\nМакс: {max_num}\nМин: {min_num}\nСреднее: {avg}\nВыше среднего: {above}")