from PIL import Image
from flask import send_file
import os
import random
import re
from os.path import abspath, join
from io import BytesIO


def create_word_dictionaries(char_list):
    """
    Takes in a list of character image paths.
    Converts paths to PIL Image objects.
    Groups character image objects into words and stores them in dictionaries.
    Returns a list of word dictionaries.
    """
    images = []

    for char in char_list:
        if char != ' ':
            images.append(Image.open(join(os.getcwd(), abspath(char)))) 
        else:
            images.append(char)

    word_list = []
    word_dict = {}
    char_count = 0
    sum_of_width = 0
    max_height = 0
    for char in images:
        if char == ' ':
            word_dict['height'] = max_height
            word_dict['width'] = sum_of_width
            word_list.append(word_dict)
            word_dict = {}
            sum_of_width = 0
            max_height = 0
            char_count = 0
        else:
            width, height = char.size
            sum_of_width += width
            if height > max_height:
                max_height = height
            word_dict[char_count] = char
            char_count += 1

    word_dict['height'] = max_height
    word_dict['width'] = sum_of_width
    word_list.append(word_dict)

    return word_list


def create_lines(word_dicts):
    """
    Takes in a list of word dictionaries.
    Determines how many words can fit on each line.
    Returns a list of lines.
    """
    max_width = 900
    space = 40
    line_width = 0
    line_height = 0
    line_count = 0
    words = []
    line = {}
    all_lines = {}

    for word in word_dicts:
        if word['width'] + line_width > max_width:
            line['words'] = words
            line['width'] = line_width
            line['height'] = line_height
            all_lines[line_count] = line
            line_count += 1
            line_width = 0
            line_height = 0
            words = []
            line = {}
        words.append(word)
        line_width += word.get('width')
        if word.get('height') > line_height:
            line_height = word.get('height')
        if space + line_width < max_width:
            line_width += space
    line['words'] = words
    line['width'] = line_width
    line['height'] = line_height
    all_lines[line_count] = line

    return all_lines


def determine_background(lines):
    """
    Takes in a list of lines.
    Returnes the width and height of the background image needed for final image.
    """
    max_width = 0
    sum_of_height = 0

    for i in range(len(lines)):
        if lines[i].get('width') > max_width:
            max_width = lines[i].get('width')
        sum_of_height += lines[i].get('height') + 20

    max_width += 20
    sum_of_height += 10

    return (max_width, sum_of_height)


def compose_image(width, height, lines):
    """
    Takes in the width and height of the final image.
    Takes in a list of lines.
    Composes the final image.
    Returns a PIL Image object.
    """
    background = Image.new('RGBA', (width, height), (38, 38, 38, 255))

    bg_width = width
    bg_height = height
    v_buffer = 10

    # For each line
    for i in range(len(lines)):
        line_height = lines[i]['height']
        line_width = lines[i]['width']
        horizontal_buffer = (bg_width - line_width) // 2
        # For each word
        for j in range(len(lines[i]['words'])):
            word = lines[i]['words'][j]
            # For each char
            for k in range(len(word) - 2):
                char = word[k]
                char_w, char_h = char.size
                offset = (horizontal_buffer,
                          ((line_height - char_h) // 2 + v_buffer))
                background.paste(char, offset)
                horizontal_buffer += char_w
            horizontal_buffer += 40
        v_buffer += line_height + 10

    return background


def serve_pil_image(pil_img):
    """
    Takes in a PIL Image object.
    Stores the image in a BytesIO object.
    Returns a command to send the image as a byte stream.
    """
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


base_punctuation_path = 'app/assets/punctuation_1'

special_chars = {
    '\'': f'{base_punctuation_path}/apostrophe_1.png',
    '\"': f'{base_punctuation_path}/doublequote_straight_1.png',
    '\n': ' ',
    '\t': ' ',
    '\n': ' ',
    ' ': ' ',
    '@': f'{base_punctuation_path}/at_1.png',
    '$': f'{base_punctuation_path}/money_1.png',
    '#': f'{base_punctuation_path}/pound_1.png',
    ':': f'{base_punctuation_path}/colon_1.png',
    ';': f'{base_punctuation_path}/semicolon_1.png',
    '.': f'{base_punctuation_path}/period_1.png',
    '…': f'{base_punctuation_path}/ellipses_1.png',
    '-': f'{base_punctuation_path}/hyphen_1.png',
    '*': f'{base_punctuation_path}/asterisk_1.png',
    '&': f'{base_punctuation_path}/ampersand_1.png',
    '%': f'{base_punctuation_path}/percentage_1.png',
    '!': f'{base_punctuation_path}/exclaimation_1.png',
    '?': f'{base_punctuation_path}/questionmark_1.png',
    ',': f'{base_punctuation_path}/comma_1.png',
    '‘': f'{base_punctuation_path}/apostrophe_1.png',
    '’': f'{base_punctuation_path}/apostrophe_1.png',
    '”': f'{base_punctuation_path}/doublequote_straight_1.png',
    '“': f'{base_punctuation_path}/doublequote_straight_1.png',
    }


def generate_paths(query_string):
    query_string = query_string.lower()
    path_list = []
    regex_object = re.compile(r'[a-z0-9]')
    
    for char in query_string:
        rand = random.randint(1, 4)
        base_letter_path = 'app/assets/'
        
        match_object = regex_object.search(char)
        
        if match_object:
            path_list.append(f'{base_letter_path}{char}_{rand}.png')
        elif char in special_chars:
            path_list.append(special_chars[char])
        else:
            path_list.append(' ')

    return path_list


def create_note(query_string):
    paths = generate_paths(query_string)
    words = create_word_dictionaries(paths)
    lines = create_lines(words)
    width, height = determine_background(lines)
    image = compose_image(width, height, lines)
    return serve_pil_image(image)