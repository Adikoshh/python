A = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61]
B = [67, -56, 0, 1, 3, 9, 45, 64, -15, 64]
print('Array A: ', A)
print('Array B: ', B)
C = []
for i in range(10):
    C.append(A[i])
    A[i] = B[i]
    B[i] = C[i]

print('Array A: ', A)
print('Array B: ', B)