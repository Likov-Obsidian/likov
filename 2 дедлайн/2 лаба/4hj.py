n = int(input("Введите высоту пирамиды: "))
i = 1

while i <= n:
    spaces = "  " * (n - i)
    left = ""
    j = 1
    while j <= i:
        left += str(j)
        j += 1
    right = ""
    k = i - 1
    while k >= 1:
        right += str(k)
        k -= 1
    
    print(spaces + left + right)
    i += 1