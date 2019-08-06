import os
from os.path import abspath, join
import random

"""
input = a string, the message you want to enter

special_ chars = a dictionary of punctuation marks that is accessed with the query

generate paths = a function that builds dynamic pathing to each character in the query, so that the images can be used in a personalized ransom note
"""

base_punctuation_path = 'app/assets/punctuation_1'

special_chars = {
    '&': f'{base_punctuation_path}/ampersand_1.png',
    '*': f'{base_punctuation_path}/asterix_1.png',
    '@': f'{base_punctuation_path}/at_1.png',
    '\"': f'{base_punctuation_path}/doublequote_straight_1.png',
    '!': f'{base_punctuation_path}/exclaimation_1.png',
    '$': f'{base_punctuation_path}/money_1.png',
    '.': f'{base_punctuation_path}/period_1.png',
    '#': f'{base_punctuation_path}/pound_1.png',
    '?': f'{base_punctuation_path}/questionmark_1.png',
    ' ': ' ' 
}


def generate_paths(query_string):
    path_list = []
    for char in query_string:

        rand = random.randint(1, 3)
        base_letter_path = 'app/assets/'
        
        letter = f'{base_letter_path}{char}_{rand}.png'

        if char in special_chars:
            path_list.append(special_chars[char])
            continue

        path_list.append(letter)
    print(path_list)
        
query = input('Enter your message here: ')
generate_paths(query)
