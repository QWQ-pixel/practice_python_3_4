from PIL import Image, ImageDraw


def gardient(color):
    size_x, size_y = 512, 200
    new_color = (0, 0, 0)
    new_image = Image.new("RGB", (size_x, size_y), new_color)
    draw = ImageDraw.Draw(new_image)
    if color.lower() == 'r':
        for i in range(512):
            draw.line((i, 0, i, 199), fill=(i // 2, 0, 0), width=2)
    if color.lower() == 'g':
        for i in range(512):
            draw.line((i, 0, i, 199), fill=(0, i // 2, 0), width=2)
    if color.lower() == 'b':
        for i in range(512):
            draw.line((i, 0, i, 199), fill=(0, 0, i // 2), width=2)
    new_image.save("gardient.png", "PNG")


# gardient('R')
