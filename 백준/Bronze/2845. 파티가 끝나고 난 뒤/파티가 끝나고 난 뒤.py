L, P = map(int, input().split())
a = L * P
par = list(map(int, input().split()))
for i in par:
        print(i-a, end = ' ')