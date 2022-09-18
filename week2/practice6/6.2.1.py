n = int(input('Enter the length of array: '))
a = []
for i in range(n):
    print('Enter the element: ')
    a.append(int(input()))
print(min(a))
for i in range(n):
    if a[i] == min(a):
        print(i)