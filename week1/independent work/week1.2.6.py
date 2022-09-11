x = 1
for x in range(101):
    if x != 50 and x != 99:
        print(x);
        x = x +1;

n = 1;
while n in range(0, 101):
    if n < 50:
        print(n);
        n = n+1;
    elif n > 50 and n != 99:
        print(n);
        n = n+1;