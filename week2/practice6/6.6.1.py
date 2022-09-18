a = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61, -45, 53]
less = 0
greater = 0
print('Maximum of the array: ', max(a))
for i in range(len(a)):
    if a[i] < max(a):
        if a[i] > a[i-1]:
            less = a[i]
        else:
            less = a[i-1]
    else:
        if (a[i] > a[i-1]):
            greater = a[i]
            if a[i] == max(a):
                print('There is no element greater than maximum')
        else:
            greater = a[i-1]
            if a[i-1] == max(a):
                print('There is no element greater than maximum')
print('Element less than maximum: ', less)