a = str(input('Enter the text: '))
count = 0
for i in a:
    if i == 'a' or i == 'A':
        a.replace('a', ' ')
        count += 1
print(count)