n = int(input('Enter the size of list(at least 2): '))
a = []
for i in range(n):
    a.append(input('Enter the elements: '))
b = 0
b = a[0]
a[0] = a[n-1]
a[n-1] = b
print(a)