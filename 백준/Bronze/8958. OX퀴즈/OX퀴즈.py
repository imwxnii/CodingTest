n = int(input())

for _ in range(n):
    sum = 0
    x = 1
    a = list(input())
    for i in a:
        if i == 'O':
            sum += x
            x += 1
        elif i == 'X':
            x = 1
    print(sum)