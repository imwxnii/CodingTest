a = int(input())
for _ in range(a):
    x, y = input().split()
    for i in y:
        for j in range(int(x)):
            print(i, end = '')
    print('')