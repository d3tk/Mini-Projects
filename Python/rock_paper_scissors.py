# rock paper scissors project 
# Start: January 21st 2022
# End: January 21st 2022
# Declan Kutscher github: d3tk

import random as rd

def play():
    user = input('Enter Rock(r), Scissors(s) or Paper(p)')
    print('Your selection was ', user)
    comp = rd.choice(['r', 's', 'p'])
    print('The computer chose ', comp)

    if user == comp:
        print('It\'s a tie!')
    elif is_win(user, comp):
        print('You won!')
    else: 
        print('You lost. ')

def is_win(user, comp):
    if (user == 'r' and comp == 's') or (user == 's' and comp == 'p') \
        or (user == 'p' and comp == 'r'):
        return True

    
