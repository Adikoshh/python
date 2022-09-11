def check_pass (pswd):
    if len(pswd) == 8:
        if any(c for c in pswd if c.islower()):
            if any(c for c in pswd if c.isupper()):
                if '-' in pswd or '*' in pswd or '#' in pswd:
                    print('The password is perfect');
                else:
                    print('Your password must contain one of special characters: "-", "*", "#"');
            else:
                print('Your password must contain upper case letters');
        else:
            print('Your password must contain lower case letters');
    else:
        print('Your password must contain only 8 characters.');

password = str(input('Please, enter your password: '));
print(check_pass(password));
