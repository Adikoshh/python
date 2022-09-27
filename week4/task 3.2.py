n=int(input('Enter the number of rows: '))
m=int(input('Enter the number of columns: '))
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print('Enter the elements: ')
        b.append(int(input()))
    a.append(b)

print('Final array: ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

max = a[0][0]
ie = je = 0
for i in range(m):
    for j in range(n):
        if a[i][j] > max:
            max = a[i][j]
            ie = i
            je = j
a[0], a[ie] = a[ie], a[0]
a[0][0], a[0][je] = a[0][je], a[0][0]
for row in a:
    print(*map('{:2d}'.format, row))
