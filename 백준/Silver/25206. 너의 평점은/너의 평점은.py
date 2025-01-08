grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']

x = 0
y = 0

for _ in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        x += b
        y += b * grade[rating.index(c)]

print(y / x)