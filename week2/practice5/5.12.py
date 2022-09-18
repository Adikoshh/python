a = str(input('Enter the text: '))
newa = ''
for i in a.split():
    if i.endswith('i'):
        print(i, " ")