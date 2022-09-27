def division(n):
    for i in range(n):
        if divide(i) == True:
            print(i)


def divide(n):
    temp = n
    while (temp > 0):

        digit = temp % 10
        if ((digit != 0 and n % digit == 0) == False):
            return False

        temp = temp // 10

    return True


n = int(input("enter the numb: "))
division(n)