symbol = input("Символ: ")
height = int(input("Высота: "))
width = int(input("Ширина: "))

i = 0
while i < height:
    j = 0
    line = ""
    while j < width:
        line += symbol
        j += 1
    print(line)
    i += 1