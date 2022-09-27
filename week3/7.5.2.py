def printt(a):
    for i in a:
        print(i, end=', ')

def division(a):
    b = []
    for i in range(1, (a+1)):
        if a%i==0:
            b.append(i)
    printt(b)


a = int(input('Enter the number: '))
division(a)