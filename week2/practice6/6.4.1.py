a = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61, -45, 53]
print(max(a))
for i in range(len(a)):
    if a[i] == min(a):
        print(i)