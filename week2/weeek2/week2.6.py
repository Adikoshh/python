n = int(input('Enter the size of list: '))
a = []
for i in range(n):
    a.append(str(input('Enter the elements: ')))

def all_eq(a):
    newa = []
    m = len(max(a, key = len))
    for j in a:
        if len(j) != m:
            for k in range(m-len(j)):
                j = j + "_"
            newa.append(j)
        else:
            newa.append(j)
    print(newa)

all_eq(a)