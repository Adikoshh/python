a = [26, 10, 0, -3, -15, 61, 74, 99, 12, 14, 51]
b = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])
print(max(b))