from PIL import Image


def makeanagliph(filename, delta):
    image = Image.open(filename)
    pixels = image.load()
    x, y = image.size
    new_image = Image.new('RGB', (x, y), (255, 255, 255))
    pixels2 = new_image.load()
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            if i - delta >= 0:
                r1, g1, b1 = pixels[i - delta, j]
                pixels2[i, j] = r1, g, b
            else:
                g, b = pixels[i, j][1:]
                pixels2[i, j] = 0, g, b
    new_image.save('res.jpg')


# makeanagliph('image.jpg', 10)
