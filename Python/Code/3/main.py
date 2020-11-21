import re
from sys import argv
script, phone, email = argv

rePhone = '^(\+880)?-\d{3}-\d{3}-\d{4}$'
reEmail = '^[a-z0-9]+[\._]?[a-z0-9]+[@][a-z]+[.]\w{2,3}$'

def findPhoneOperator():
    phone_split = phone.split('-', 4)
    phone_code = phone_split[1]
    for i in range(0, len(phone_code)):
        if i == 1:
            operator_checker = phone_code[i]
            if operator_checker == '7' or operator_checker == '3':
                print('It is Grameen number')
            elif operator_checker == '8':
                print('It is Robi number')
            elif operator_checker == '6':
                print('It is Airtel number')
            elif operator_checker == '9' or operator_checker == '4':
                print('It is Banglalink number')
            elif operator_checker == '5':
                print('It is Teletalk number')
            else:
                print('Unknown mobile operator')

def findEmail():
    email_split = email.split('@', 2)
    username = email_split[0]
    email_code = email_split[1]
    if email_code == 'hotmail.com':
        print('Hotmail is not acceptable.')
    else:
        print('Username: {0}'.format(username))
        print(f'Domain name: {email_code}')

if (re.search(rePhone, phone)) and (re.search(reEmail, email)):
    print('Output:')
    findPhoneOperator()
    findEmail()
elif (not re.search(rePhone, phone)) and (re.search(reEmail, email)):
    print('Invalid phone number!')
    print('Required format: +880-XXX-XXX-XXXX')
elif (re.search(rePhone, phone)) and (not re.search(reEmail, email)):
    print('Invalid email!')
    print('Required format: test@test.com')
else:
    print('Invalid phone number!')
    print('Required format: +880-XXX-XXX-XXXX')
    print('Invalid email!')
    print('Required format: test@test.com')