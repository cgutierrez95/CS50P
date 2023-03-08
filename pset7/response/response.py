from validator_collection import validators, checkers, errors

mail = input("What's your email address? ")

try:
    email_address = validators.email(mail)
    print('Valid')
except:
    print('Invalid')
