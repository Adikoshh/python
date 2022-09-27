def smallestInRow(mat):
    minm = min(mat)
    return minm


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
minm = []
for i in range(n):
    minm.append(smallestInRow(a[i]))
print(minm)

for i in range(len(minm)):
        if minm[i]%2==0:
            minm[i]=0
        else:
            minm[i]=1
print(minm)
