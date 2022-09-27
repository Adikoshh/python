def armStrong(n):
    for num in range(1, 1000):
        order = len(str(num))
        sum = 0
        a = num
        while a > 0:
            digit = a % 10
            sum += digit ** order
            a //= 10

        if num == sum:
            print(num)


n = int(input("enter the n: "))
armStrong(n)