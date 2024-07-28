a = int(input())
score = list(map(int, input().split()))
b = max(score)
sum = 0
for i in range(a):
    score[i] = score[i]/b*100
    sum += score[i]
print(sum / a)