roman = input("Введите римское число: ").upper()
roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
values = []
for i in range(len(roman)):
    current_char = roman[i]
    if current_char not in roman_dict:
        print("некорректный символ")
        break
    current_value = roman_dict[current_char]
    if i + 1 < len(roman):
        next_value = roman_dict.get(roman[i + 1], 0)
        if current_value < next_value:
            values.append(-current_value)
        else:
            values.append(current_value)
    else:
        values.append(current_value)
if len(values) == len(roman):
    result = sum(values)
    print(f"{roman} = {result}")