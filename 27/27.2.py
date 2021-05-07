import random


def image_negative(pixels, i, j):
    """Негатив"""
    r = pixels[i, j][0]
    g = pixels[i, j][1]
    b = pixels[i, j][2]
    return int(255 - r), int(255 - g), int(255 - b)


def image_noises(pixels, i, j):
    """Добавляет шумы"""
    rand = random.randint(-70, 70)
    r = pixels[i, j][0] + rand
    g = pixels[i, j][1] + rand
    b = pixels[i, j][2] + rand
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    return r, g, b
