def is_alive(health):
    if health == 0 or health<0:
        return False;
    else:
        return True;

healthh = int(input('Enter the health status: '));
print(is_alive(healthh));
