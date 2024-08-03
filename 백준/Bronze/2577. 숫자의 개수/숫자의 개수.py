a = int(input())
b = int(input())
c = int(input())

n = str(a*b*c)

print(n.count('0'))
for i in range(1, 10):
    print(n.count(str(i)))