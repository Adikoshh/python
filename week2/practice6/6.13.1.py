a = []
n = 10
for i in range(n):
    a.append(int(input('Enter the array elements(10): ')))
for i in range(n):
    if a[i] == a[i-1]:
        print(a[i], i)
