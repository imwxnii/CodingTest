five = []
length = []

for _ in range(5):
    word = input()
    five.append(word)
    length.append(len(word))

result = ''

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            result += five[j][i]

print(result)