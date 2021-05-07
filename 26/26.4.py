import random
from PIL import Image, ImageDraw


def drawColor():

    R = random.randrange(0, 256)
    B = random.randrange(0, 256)
    G = random.randrange(0, 256)

    return R, G, B


def draw_name():
    new_color = (0, 0, 0)
    new_image = Image.new("RGB", (512, 200), new_color)
    draw = ImageDraw.Draw(new_image)
    size = 512/4
    for x in range(4):
        for y in range(2):
            x1 = x * size
            y1 = y * size
            x2 = x1 + size
            y2 = y1 + size
            draw.rectangle((x1, y1, x2, y2), fill=drawColor())
    draw.line((10, 20, 10, 512), fill='black', width=10)
    draw.ellipse((10, 20, 90, 100), fill='aquamarine', width=10)
    draw.ellipse((10, 100, 110, 200), fill='darksalmon', width=10)
    draw.line((150, 0, 0, 512), fill='chartreuse', width=15)
    draw.line((200, 800, 150, 0), fill='deeppink', width=3)
    draw.line((160, 150, 60, 150), fill='deeppink', width=20)
    draw.line((300, 30, 30, 512), fill='saddlebrown', width=20)
    draw.line((300, 800, 300, 20), fill='palegreen', width=20)
    draw.ellipse((400, 20, 500, 110), outline='snow', width=15)
    draw.line((512, 80, 30, 500), fill='cyan', width=15)
    draw.line((500, 20, 470, 500), fill='deepskyblue', width=15)

    new_image.save('res.jpg')


draw_name()
