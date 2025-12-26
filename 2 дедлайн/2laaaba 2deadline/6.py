n = int(input("Введите n (нечетное): "))
matrix = [[0]*n for _ in range(n)]
x = y = n // 2
num = 1
matrix[x][y] = num
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
step = 1
dir_idx = 0
while num < n*n:
    for _ in range(2):
        dx, dy = dirs[dir_idx]
        for _ in range(step):
            x += dx
            y += dy
            num += 1
            if num > n*n:
                break
            matrix[x][y] = num
        dir_idx = (dir_idx + 1) % 4
    step += 1
for row in matrix:
    for val in row:
        print(f"{val:3}", end=" ")
    print()