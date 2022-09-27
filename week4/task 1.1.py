n=3
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print('Enter the element:')
        b.append(int(input()))
    a.append(b)
c = 0
d = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] > 0:
            d += a[i][j]
            c+= 1
print("Number of positive: " , c)
print("Sum: " , d)
