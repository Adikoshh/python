def occt(a):
    if a > 0:
        return oct(a)
    else:
        return 'There is no way.'

a = int(input('Enter the number: '))
print(oct(a))