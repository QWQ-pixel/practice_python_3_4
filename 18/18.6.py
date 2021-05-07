def line(s, t):
    x, y = float(t.split(';')[0]), float(t.split(';')[-1])
    sep = s.replace('x', ' ').split()
    print(y == float(sep[0]) * x + float(sep[-1]))

