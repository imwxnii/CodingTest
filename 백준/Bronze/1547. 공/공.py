m = int(input())
list = [1, 0, 0]
for _ in range(m):
    x, y = map(int, input().split())
    temp = list[x-1]
    list[x-1] = list[y-1]
    list[y-1] = temp
print(list.index(1)+1)