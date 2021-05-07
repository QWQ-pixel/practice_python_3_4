def equation(a, b):
    x1, y1 = float(a.split(';')[0]), float(a.split(';')[-1])
    x2, y2 = float(b.split(';')[0]), float(b.split(';')[-1])
    if x1 - x2 > 0:
        k = (y1 - y2) / (x1 - x2)
    else:
        k = 0
    b = y2 - k * x2
    if k == 0:
        print(b)
    elif b == 0:
        print(k)
    else:
        print(k, b)



