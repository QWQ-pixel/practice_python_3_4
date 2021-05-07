import random


def find_pi():
    k, num = 0.0, 500000
    for i in range(num):
        x, y = random.random(), random.random()
        k += (x * x + y * y < 1.0)
    print(4 * k / num)


find_pi()
