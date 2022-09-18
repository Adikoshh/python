a = []
n = 15
for i in range(n):
    a.append(int(input('Enter the array elements(15): ')))
for i in range(15):
    if a[i] < 10:
        a[i] = 0
    if a[i] > 20:
        a[i] = 1

print(a)