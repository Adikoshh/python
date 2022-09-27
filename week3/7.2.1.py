import math
def areaT(a):
    areaTr = ((1/2)*a*a*math.sin(math.radians(60)))
    return areaTr
def area(a):
    area = 6 * areaT(a)
    print(round(area, 3))

aa = int(input('Enter a: '))
area(aa)