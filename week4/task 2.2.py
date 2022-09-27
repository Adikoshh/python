n=int(input('Enter the number of rows: '))
m=int(input('Enter the number of columns :'))
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print('Enter the element: ')
        b.append(int(input()))
    a.append(b)

print('Final array: ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
for i in range(n):
    temp = a[i][0]
    a[i][0] = a[i][m-1]
    a[i][m-1] = temp

for i in range(n):
    for j in range(m):
        print("%2d " % a[i][j], end=' ')
    print()
