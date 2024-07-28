a, b = map(int, input().split())
c = [0 for d in range(a)]

for _ in range(b):
    i, j, k = map(int, input().split())
    for z in range(i-1, j):
        c[z] = k

for x in c:
    print(x, end = ' ')