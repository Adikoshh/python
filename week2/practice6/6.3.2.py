a = [1, 21, -13, -9, 4, 4, 0, -7]
for i in range(len(a)):
    if a[i] < 15:
        a[i] = (a[i] * a[i])
print(a)