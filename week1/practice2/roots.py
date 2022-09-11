import math;
a = float(input('a ='));
b = float(input('b ='));
c = float(input('c ='));
D = (b*b)-(4*a*c);
if D<0 :
    print('This equation has no real roots');
elif D == 0:
    x = (-b + math.sqrt(D))/(2*a);
    print ('This equation has one root: ', x);
else:
    x1 = (-b + math.sqrt(D))/(2*a);
    x2 = (-b - math.sqrt(D))/(2*a);
    print ('This equation has two roots: ', x1, ',', x2);
