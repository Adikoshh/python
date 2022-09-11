import math;
f = str(input('Which one: rectangle, triangle, circle? Please, write only first letter in lower case. '));
if f == 'r' :
    a = int(input('The lenght of the first side:'));
    b = int(input('The lenght of the second side:'));
    areaR = a*b;
    print(areaR);
elif f == 't':
    aT = int(input('The lenght of the first side:'));
    bT = int(input('The lenght of the second side:'));
    cT = int(input('The lenght of the third side:'));
    p = (aT+bT+cT)/2;
    areaT = math.sqrt(p*(p-aT)*(p-bT)*(p-cT));
    print (areaT);
else:
    R = int(input('The radius of circle:'));
    areaC = 2*math.pi*R;
    print (areaC);
