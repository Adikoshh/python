number = 0;
sum = 0;
try:
    sequence = [];  
    while True:
        sequence.append(int(input('Enter the sequence: ')));
        number += 1;
except:
    print(sequence);
    print(number);