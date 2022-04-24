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

            print('confirm password')
            confirm_password = input()


            while confirm_password != created_user_password:
            print("invalid password did not match")
            print("enter your password")
            created_user_password = input()
            print("confirm your password")
            confirm_password = input()
        else:
            print(f"congratulations {created_user_name}! account creation successful")  
            print('\n')  
            print("proceed to login")
            print("Username")
            entered_username = input()
            print("your password")
            entered_password = input()

        while entered_username != created_user_name or entered_password != created_user_password:
            print("Invalid username or password")    
            print("Username")
            entered_username = input()
            print("Your password")
            entered_password = input()

        else:
            print(f"welcome (entered_username) to your account")  
            print('\n')  

        






