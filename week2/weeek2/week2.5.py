import math
n = int(input('Enter the size of list: '))
a = []
for i in range(n):
    a.append(int(input('Enter the elements: ')))

def list_sort():
    for i in range(n):
        math.fabs(a[i])
    a.sort(reverse=True)
    print(a)

list_sort()