# Hangman project 
# Start: January 21st 2022
# End: January 21st 2022
# Declan Kutscher github: d3tk

import random as rd
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = rd.choice(words)
    while '-' in word or ' ' in word:
        word = rd.choice(words)
    
    return word.upper()

def hangman():
    x = input("Random word or user generated word. 1 for random or enter a word. No spaces or - please.")
    if x is '1':
        word = get_valid_word(words)
    else:
        word = x.remove(' ').remove('-')
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives >0:
        print('You have', lives, 'lives  left and you have used these letters: ', ' '.join (used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict([lives]))
        print('Current word: ', word)

        user_letter = input('Insert a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(' ')
            
            else:
                lives = lives - 1
                print('\nYour letter', user_letter, 'is not in the word')
        elif user_letter in used_letters:
            print('You have already used that letter, pick another letter.')
        else:
            print('\nThat is not a valid letter.')
    
    if lives == 0:
        print(lives_visual_dict([lives]))
        print('You died, sorry. Word was: ', word)
    else:
        print('You guessed the word, congrats!')







if __name__ == '__main__':
    hangman()