import random
from user import User


def main():

    while True:
        print("welcome to password locker!!!")
        print('\n')
        print("Select a short code to navigate through:to create new user use 'nu':To login to your account 'lg' or 'ex' to exit")
        short_code = input().lower()
        print('\n')

        if short_code == 'nu':
            print('create username')
            created_user_name = input()

            print('create password')
            created_user_password = input()
