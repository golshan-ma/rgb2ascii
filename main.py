import math

import numpy as np
from PIL import Image

DENSITY = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def split(word):
    return [char for char in word]


DENSITY = split(DENSITY)
print(len(DENSITY))


def to_grayscale(image_address: str) -> Image.Image:
    img = Image.open(image_address).convert('L')
    return img


def to_ascii(filename: str, destiny_name: str):
    I = np.asarray(to_grayscale(filename))
    n = []
    for y in I:
        ny = []
        for x in y:
            i = math.floor(x / 3.65)
            ny.append(DENSITY[i])
        n.append(ny)
    big_str = ''
    for t in n:
        z = ''.join(t)
        big_str += z + '\n'

    f = open(f'{destiny_name}.txt', 'w')
    f.write(big_str)
    f.close()


to_ascii('download (1).png', 'des')
