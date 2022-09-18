a = [1, 13, 0, 6, 7, 7, 0, 10, 64, 23, 0]
s = 0
for i in a:
    s += i
mean = (s/(len(a)+1))
for i in range(len(a)):
    if a[i] > mean:
        a[i] = 1
print(mean)
print(a)