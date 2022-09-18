a = [26, 10, 0, -3, -15, 61, 74, 99, 12, 14, 51]
b = []
for i in range(len(a)):
    if a[i] < 10 and a[i] % 2 == 0:
        b.append(a[i])
b.reverse()
if len(b) == 0:
    print('There is no such elements.')
else:
    print(b)