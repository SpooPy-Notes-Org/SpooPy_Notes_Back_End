from PIL import Image
import os
from os.path import abspath, join


def create_word_dictionaries(char_list):
    """
    Takes in a list of Image instances.
    Returns a list of word dictionaries.
    """
    char_count = 0
    word_dict = {}
    word_list = []
    sum_of_width = 0
    max_height = 0
    for char in char_list:
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
    Returns a list of lines.
    """
    max_width = 600
    space = 10
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
    max_width = 0
    sum_of_height = 0

    for i in range(len(lines)):
        if lines[i].get('width') > max_width:
            max_width = lines[i].get('width')
        sum_of_height += lines[i].get('height') + 10

    max_width += 20
    sum_of_height += 10

    return (max_width, sum_of_height)


def compose_image(width, height, lines):
    background = Image.new('RGBA', (width, height), (255, 255, 255, 255))

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
            horizontal_buffer += 10
        v_buffer += line_height + 10

    background.save('output.png')

    return join(os.getcwd(), 'output.png')


if __name__ == "__main__":
    images = [
        'assets/style_1/t_1.png',
        'assets/style_1/h_1.png',
        'assets/style_1/i_1.png',
        'assets/style_1/n_1.png',
        'assets/style_1/k_1.png'
    ]

    result = create_word_dictionaries(images)

    result = create_lines(result)

    x, y = determine_background(result)

    compose_image(x, y, result)