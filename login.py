# login schematic project 
# Start: January 20th 2022
# End: January 21st 2022
# Declan Kutscher github: d3tk

import time

def create_account(accounts):
    print('Create an account...')
    wrkng = True
    while wrkng == True:
        username = input('Username: ')
        if username not in accounts.keys():
            password = input('Password: ')
            accounts[username] = password
            print('Account Creation successfull')
            wrkng = False
        else:
            print("Username already in use, try again.")
        
    
def update_account(accounts):
    print('Update an account')
    wrkng = True
    while wrkng:
        username = input('Username: ')
        if username not in accounts.keys():
            user = input('Invalid username, try again. Quit by entering Q, continue by entering anything else')
            if user == 'Q':
                return 
        else:
            password = input('Password: ')
            trying = True
            while trying:
                if accounts.get(username) != password:
                    user = input('Invalid password, try again. Quit by entering Q, continue by entering anything else')
                    if user == 'Q':
                        trying = False
                        return
                else:
                    new_password = input('Enter new password: ')
                    if new_password != accounts.get(username):
                        accounts[username] = new_password
                        print('Account updated')
                        trying = False
                        return
                password = input('Password: ')              


    
def login(accounts):
    print('Login: .... ')
    wrkng = True
    while wrkng:
        username = input('Username: ')
        if username not in accounts.keys():
            user = input('Invalid username, try again. Quit by entering Q, continue by entering anything else')
            if user == 'Q':
                return 
        else:
            trying = True
            while trying:
                password = input('Password: ')
                if accounts.get(username) != password:
                    user = input('Invalid password, try again. Quit by entering Q, continue by entering anything else')
                    if user == 'Q':
                        trying = False
                        return
                else: 
                        print('Access granted')
                        print('Please wait')
                        time.sleep(5)
                        print('Ok... Loading...')
                        time.sleep(1)
                        print('...')
                        time.sleep(1)
                        print('...')
                        print('Log in Successfull')
                        trying = False
                        wrkng = False





if __name__ == '__main__':
    accounts = {}
    answer = input('What would you like to do? 1. Create an account 2. Update an account 3. Log in or STOP. Insert a number or STOP.')

    while answer.lower() != "stop":
        if answer == '1':
            create_account(accounts)
        elif answer == '2':
            update_account(accounts)
        elif answer == '3':
            login(accounts)
        else:
            print('Invalid selection, try again!')
        answer = input('What would you like to do? 1. Create an account 2. Update an account 3. Log in or STOP. Insert a number or STOP.')
