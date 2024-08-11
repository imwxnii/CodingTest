m = ['x', 'y']
for i in range(2):
    a = int(input())
    b = int(input())
    c = int(input())
    m[i] = (a*3) + (b*2) + (c*1)
if m[0] > m[1]:
    print('A')
elif m[0] < m[1]:
    print('B')
else:
    print('T')