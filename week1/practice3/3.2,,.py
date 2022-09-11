def season_events(number_of_month):
    if number_of_month == 3 or number_of_month == 4 or number_of_month == 5:
        print('You were born in ', number_of_month, '. Birds sang beautiful songs.');
    elif number_of_month == 6 or number_of_month == 7 or number_of_month == 8:
        print('You were born in ', number_of_month, '. The sun shone brighter than ever.');
    elif number_of_month == 9 or number_of_month == 10 or number_of_month == 11:
        print('You were born in ', number_of_month, '. The harvest was incredible.');
    elif number_of_month == 3 or number_of_month == 4 or number_of_month == 5:
        print('You were born in ', number_of_month, '. White snow fell outside the window.');
    else:
        print('You need to enter the real number of the month');

number_of_month = int(input('Enter the number of the month of your birth: '))
print(season_events(number_of_month));
