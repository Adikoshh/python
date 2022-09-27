import math
def mean(arr):
    mean = 0
    sum = 0
    for i in range(len(arr)):
        mean += (arr[i]/len(arr))
        sum += arr[i]
    print(sum, ',', round(mean, 3))

a = [15, 25, 21, 64, 34, 97, 84, 61]
b = [54, 0, 31, 74, 89, 9, 0]
c = [52, 40, 49, 94, 3, 70, 69, 4, 35, 21, 5]
mean(a)
mean(b)
mean(c)