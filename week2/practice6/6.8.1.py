a = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61, -45, 53]
p = 1
s = 0
for i in range(len(a)):
    p = p*a[i]
    s += a[i]
print('Product of the array: ', p)
print('Sum of the array: ', s)