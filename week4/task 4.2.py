n=int(input('Enter the number of rows: '))
m=int(input('Enter the number of columns: '))
a=[]
for i in range(m):
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

a = [[1 if x>0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x<=i else '' for x in range(len(a[i]))],'')


