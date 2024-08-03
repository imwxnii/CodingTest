a = int(input())
for i in range(a):
    h, w, n = map(int, input().split( ))
    floor = n % h 
    l = (n // h) + 1
    if floor == 0:
        floor = h
        l -= 1
    print(floor*100+l)