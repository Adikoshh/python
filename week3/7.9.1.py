def Sum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


def sumC(n, sum):
    repeat = -1
    while n >= 0:
        n -= sum
        repeat += 1
    return repeat


n = int(input("Enter the number: "))
sum = Sum(n)
print(sum)
print(sumC(n, sum))