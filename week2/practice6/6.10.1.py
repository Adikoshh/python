a = []
n = 10
d = []
for i in range(n):
    a.append(int(input('Enter the array elements(10): ')))
for i in range(n):
    if a[i] == a[i-1]:
        d.append(a[i])

if len(d) == 0:
    print('There is no duplicate elements.')
else:
    print('Duplicate elements: ', d)