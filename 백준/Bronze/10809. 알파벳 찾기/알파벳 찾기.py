x = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in x:
        print(x.index(i), end = ' ')
    else:
        print( -1, end = ' ')