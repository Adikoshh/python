n=3
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print('Enter the element: ')
        b.append(int(input()))
    a.append(b)
def magic(a):
    n = 3
    d1 = 0
    d2 = 0
    for i in range(n):
        d1 += a[i][i]
        d2 += a[i][n - i - 1]
    if not (d1 == d2):
        return False
    for i in range(n):
        rows = 0
        cols = 0
        for j in range(n):
            rows  += a[i][j]
            cols += a[j][i]
        if not (rows  == cols == d1):
            return False

    return True

if (magic(a)):
    print("Magic Square")
else:
    print("Not a magic Square")
