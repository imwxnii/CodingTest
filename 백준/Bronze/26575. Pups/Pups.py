n = int(input())
for _ in range(n):
    x, y, z = map(float, input().split())
    print('$%.2f' % float(x*y*z))