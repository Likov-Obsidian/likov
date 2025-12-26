text = input("Введите текст: ")
punctuation = ".,!?:;"
l = d = p = s = 0
for char in text:
    if char.isalpha(): l += 1
    elif char.isdigit(): d += 1
    elif char in punctuation: p += 1
    elif char == " ": s += 1
print(f"букв = {l}\nцифр = {d}\nзнаков препинания = {p}\nпробелов = {s}")