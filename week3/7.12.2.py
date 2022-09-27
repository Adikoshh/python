import math

def median(a, b, c):
    median = math.sqrt(2 * (b * b + c * c) - a * a) / 2
    return median

print("enter 3 sides:")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if abs(a - b) >= c | a + b <= c:
    print("impossible triangle")
print("medians of original triangle:")
mA = median(a, b, c)
mB = median(b, a, c)
mB = median(c, a, b)
print(ma, mb, mc)
print("medians of created triangle:")
mmA = median(mA, mB, mB)
mmB = median(mB, mA, mC)
mmC = median(mC, mA, mB)
print(mmA, mmB, mmC)