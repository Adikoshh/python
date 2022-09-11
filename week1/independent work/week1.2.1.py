first = int(input('First number: '));
operation = str(input('Operation: '));
second = int(input('Second number: '));
if operation == '+':
    answer = first + second;
    print(first, '+', second, '=', answer);
elif operation == '-':
    answer = first - second;
    print(first, '-', second, '=', answer);
elif operation == '*':
    answer = first * second;
    print(first, '*', second, '=', answer);
elif operation == '/':
    if second == 0:
        print("That's impossible");
    else:
        answer = first / second;
        print(first, '/', second, '=', answer);
