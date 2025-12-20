print("Введите текст (для завершения ввода оставьте пустую строку и нажмите Enter):")
print("=" * 50)

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = " ".join(lines)

if not text.strip():