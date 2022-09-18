n = int(input('Enter the size of list: '))
a = []
for i in range(n):
    a.append(input('Enter the elements: '))

a.reverse()
print(a)