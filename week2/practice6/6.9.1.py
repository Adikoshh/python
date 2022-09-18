import math
n = int(input('Enter the length of array: '))
a = []
for i in range(n):
    print('Enter the element: ')
    a.append(int(input()))
print(math.fabs(min(a)))
a.reverse()
print(a)