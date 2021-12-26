import re

regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')


def check_email(email):
    if re.fullmatch(regex, email):
        print(f'Your email: {email} is valid.!')
    else:
        print(f'Your email: {email} not valid')


if __name__ == '__main__':
    email = 'muhammad.alamin@yahoo.com'
    check_email(email)