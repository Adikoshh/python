a = str(input('Enter the text: '))
count = 0
for i in a:
    if i == ':':
        a.replace(':', '%')
        count += 1
print(count)