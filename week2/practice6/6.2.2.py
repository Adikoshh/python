a = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61, -45, 53]
positive = []
negative = []
for i in range(len(a)):
    if a[i]>0:
        positive.append(a[i])
    elif a[i] == 0:
        positive.append(a[i])
    else:
        negative.append(a[i])
print('Positive integers: ', positive)
print('Negative integers: ', negative)