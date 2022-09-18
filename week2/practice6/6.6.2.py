a = []
n = 10
sum = 0
for i in range(n):
    a.append(int(input('Enter the array elements: ')))
for i in range(n):
    if a[i] > 5:
        sum += a[i]
print(sum)