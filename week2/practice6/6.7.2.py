a = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61, -45, 53]
m = a.index(max(a))
n = a.index(min(a))
Max = max(a)
Min = min(a)
a[m] = Min
a[n] = Max
print(a)