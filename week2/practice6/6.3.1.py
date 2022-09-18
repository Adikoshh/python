a = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61, -45, 53]
sum = 0
for i in range(len(a)):
    if a[i] % 2 != 0:
        sum += a[i]
print(a, sum)