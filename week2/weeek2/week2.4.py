n = int(input('Enter the size of list: '))
a = []
for i in range(n):
    a.append(input('Enter the elements: '))

m = int(max(a))
print(m/n)