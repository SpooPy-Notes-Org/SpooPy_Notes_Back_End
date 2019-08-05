import os
from os.path import abspath, join
import random


# contains pathing to the letters
# create dictionary
# f string... path f'{letter}_{random_num}.png'

class Letters():
    rand = random.randint(1, 3)
    base_letter_path = 'assets/'

    # letter should be set to ones from query string
    # a = f'{base_letter_path}a_{rand}'
    a = f'{base_letter_path}a_{rand}.png'
    # b = f'{base_letter_path}b_{rand}.png'
    # c = f'{base_letter_path}c_{rand}.png'

    result = join(os.getcwd(), abspath(a))

    try:
        with open(result, 'r') as file:
            contents = file.read()
            print('We have reached the thing', contents)
    except FileNotFoundError:
        print('no file found fix pathing')