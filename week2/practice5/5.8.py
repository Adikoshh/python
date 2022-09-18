a = str(input('Enter the text: '))
count = 1
#we start counting from one, because we can't split the last word, because after last word we have only a dot.
dot = 0
for i in a:
    if i == ' ':
        newa = a.split(' ')
        count += 1
print(count)