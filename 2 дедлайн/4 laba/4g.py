temperatures = [15, 17, 16, 14, 18, 20, 19, 16, 17, 21, 19, 18, 16, 15]

print("Температуры за 2 недели:", temperatures)

max_temp = max(temperatures)
min_temp = min(temperatures)
print(f"Самая высокая температура: {max_temp}°C")
print(f"Самая низкая температура: {min_temp}°C")
average_temp = sum(temperatures) / len(temperatures)
print(f"Средняя температура: {average_temp:.1f}°C")
days_above_avg = 0
for temp in temperatures:
    if temp > average_temp:
        days_above_avg += 1
print(f"Дней с температурой выше средней: {days_above_avg}")

sorted_temps = sorted(temperatures)
print("Температуры по возрастанию:", sorted_temps)

temperatures_f = []
for temp_c in temperatures:
    temp_f = temp_c * 9/5 + 32
    temperatures_f.append(round(temp_f, 1))

print("Температуры в Фаренгейтах:", temperatures_f)