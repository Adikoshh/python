a = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61, -45, 53]
odd = 1
even = 0
for i in range(len(a)):
    if a[i] % 2 != 0:
        odd = odd * a[i]
    else:
        even += a[i]
print('Sum of even elements: ', even)
print('Product of odd elements: ', odd)