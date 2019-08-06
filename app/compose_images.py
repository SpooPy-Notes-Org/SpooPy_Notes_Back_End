from PIL import Image
import os
from os.path import abspath, join
import asyncio


def determine_canvas(input_images):
    images = [Image.open(join(os.getcwd(), abspath(image))) for image in input_images]
    image_buffer = 20
    sum_width = 0
    max_height = 0

    for img in images:
        width, height = img.size
        sum_width += width
        if height > max_height:
            max_height = height

    sum_width += image_buffer
    max_height += image_buffer

    return (sum_width, max_height)


def compose_image(width, height, images):
    background = Image.new('RGBA', (width, height), (255, 255, 255, 255))
    width_offset = 10

    for img in images:
        img_width, img_height = img.size
        offset = (width_offset, (height - img_height) // 2)
        width_offset += img_width
        background.paste(img, offset)

    background.save('output.png')
    return join(os.getcwd(), 'output.png')


# Just for now
if __name__ == "__main__":
    imgsFolder = [
        'assets/style_1/t_1.png',
        'assets/style_1/h_1.png',
        'assets/style_1/i_1.png',
        'assets/style_1/n_1.png',
        'assets/style_1/k_1.png'
    ]
    images = [Image.open(join(os.getcwd(), abspath(image))) for image in imgsFolder]

    width, height = determine_canvas(imgsFolder)
    compose_image(width, height, images)