dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
n = list(input())
s = 0
for i in n:
    for j in dial:
        if i in str(j):
            num = dial.index(j) + 3
            s += num
print(s)