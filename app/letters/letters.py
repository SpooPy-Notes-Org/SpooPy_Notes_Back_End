import os
from os.path import abspath, join
import random
from PIL import Image


# contains pathing to the letters
# f string... path f'{letter}_{random_num}.png'
def read_image(path):

    try:
        img = Image.open(path)
        img.show()
    except FileNotFoundError:
        print('no file found fix pathing: you got this', path)

class Letters:

    rand = random.randint(1, 3)
    base_letter_path = 'app/assets/'

    # letter should be set to ones from query string
    a = f'{base_letter_path}a_{rand}.png'

    result = join(os.getcwd(), abspath(a))

    read_image(result)


