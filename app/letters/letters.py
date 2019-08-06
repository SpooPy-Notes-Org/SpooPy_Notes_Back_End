import os
from os.path import abspath, join
import random
from PIL import Image


# contains dynamic pathing to the letters

def accept_query_string(query):
    print(query)
    return query
    

def generate_paths(query_string):
    path_list = []
    for char in query_string:

        rand = random.randint(1, 3)
        base_letter_path = 'app/assets/'
        
        letter = f'{base_letter_path}{char}_{rand}.png'

        path_list.append(letter)
    print(path_list)
        
query = input('Enter your message here: ')
query_string = accept_query_string(query)
generate_paths(query_string)
