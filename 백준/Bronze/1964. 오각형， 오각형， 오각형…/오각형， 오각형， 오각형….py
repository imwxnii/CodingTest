a = int(input())
res = 5
plus = 7
for _ in range(1, a):
    res += plus
    plus += 3
print(res % 45678)