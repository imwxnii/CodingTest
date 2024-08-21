word = "MOBIS"
n = list(input())
for i in word:
    if i in n:
        continue
    else:
        print('NO')
        exit()
print('YES')