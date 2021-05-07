def golden_ratio(i):
    a, b, c = 0, 1, 1
    while c <= i:
        a, b = b, a + b
        c += 1
    print(b / a)

