n=int(input('Enter the number of rows :'))
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
b = "YES"
for i in range(m):
    for j in range(n):
        if a[i][j] != a[j][i]:
            b = "NO"
            break
print(b)
