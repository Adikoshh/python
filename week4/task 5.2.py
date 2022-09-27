def smallest(mat):
    minn = min(mat)
    return minn


n = int(input('Enter the number of rows: '))
m = int(input('Enter the number of columns: '))
a = []
for i in range(m):
    b = []
    for j in range(n):
        print('Enter the elements: ')
        b.append(int(input()))
    a.append(b)

print('Final array: ')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
minn = []
for i in range(n):
    minn.append(smallest(a[i]))
print(minn)

for i in range(len(minn)):
        if minn[i]%2==0:
            minn[i]=0
        else:
            minn[i]=1
print(minn)
