price = int(input('Enter the price of 1 kg of sweets: '));
total = 0;
for x in range(10):
    total += price;
    print('The price for ', x+1, ' kg of sweets: ', total )
    x+=1;
