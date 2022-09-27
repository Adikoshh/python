def printArray(arr, m, n):
    for i in range(m):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()


def sortArr(arr, m, n):
    for i in range(m):
        arr[i].sort()
    print()


n = int(input('Enter the number of rows: '))
m = int(input('Enter the number of columns: '))
a = []
for i in range(m):
    b = []
    for j in range(n):
        print('Enter the element: ')
        b.append(int(input()))
    a.append(b)

print('Final array: ')
printArray(a, m, n)

sortArr(a, m, n)
print('Changed array: ')
printArray(a, m, n)
