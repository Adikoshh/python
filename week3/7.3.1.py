import math
def hypotenuse(a, b):
    c = math.sqrt((a*a) + (b*b))
    return c
def compare(a, b, c, d):
    if hypotenuse(a, b) > hypotenuse(c, d):
        print('First is greater than second.')
    else:
        print('Second is greater than first.')

a = int(input('Enter the leg of right triangle: '))
b = int(input('Enter the leg of right triangle: '))
c = int(input('Enter the leg of right triangle: '))
d = int(input('Enter the leg of right triangle: '))
compare(a, b, c, d)