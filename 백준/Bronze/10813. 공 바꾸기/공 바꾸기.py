N, M = map(int, input().split())
list = [i for i in range(1, N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    tmp = list[x-1]
    list[x-1] = list[y-1]
    list[y-1] = tmp

for q in range(N):
    print(list[q], end = ' ')