import math
def area(f):
    if f == 'r' :
        a = int(input('The lenght of the first side: '));
        b = int(input('The lenght of the second side: '));
        area = a*b;
        print(area);
    elif f == 't':
        aT = int(input('The lenght of the first side: '));
        bT = int(input('The lenght of the second side: '));
        cT = int(input('The lenght of the third side: '));
        p = (aT+bT+cT)/2;
        area = math.sqrt((p*(p-aT)*(p-bT)*(p-cT)));
        print (area);
    else:
        R = int(input('The radius of circle: '));
        area = 2*math.pi*R;
        print (area);
        
f = str(input('Which one: rectangle, triangle, circle? Please, write only first letter in lower case: '));
area(f)