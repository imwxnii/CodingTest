gugu = []
for _ in range(9):
    n = list(map(int, input().split()))
    gugu.append(n)

max_num, max_row, max_col = 0, 0, 0
for i in range(9):
    for j in range(9):
        if max_num <= gugu[i][j]:
            max_row = i + 1
            max_col = j + 1
            max_num = gugu[i][j]

print(max_num)
print(max_row, max_col)