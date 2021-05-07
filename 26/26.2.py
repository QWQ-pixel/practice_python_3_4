from PIL import Image, ImageDraw


def board(num, size):
    size_x = size_y = num*size
    new_color = (0, 0, 0)
    new_image = Image.new("RGB", (size_x, size_y), new_color)
    draw = ImageDraw.Draw(new_image)
    color = 'black'
    for x in range(num):
        for y in range(num):
            x1 = x * size
            y1 = y * size
            x2 = x1 + size
            y2 = y1 + size
            draw.rectangle((x1, y1, x2, y2), fill=color)
            if color == 'white':
                color = 'black'
            else:
                color = 'white'
        if color == 'white':
            color = 'black'
        else:
            color = 'white'
    new_image.save("res.png", "PNG")


board(8, 50)
