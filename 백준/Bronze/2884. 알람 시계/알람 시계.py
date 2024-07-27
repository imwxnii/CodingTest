a, b = map(int, input().split())
if ((b - 45) < 0):
    if ((a - 1) == -1):
        a = 23
        b = (60 + (b-45))
    else:
        a -= 1
        b = (60 + (b-45))
else:
    b -= 45

print(str(a) + ' ' + str(b))