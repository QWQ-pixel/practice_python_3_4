from math import sqrt


def roots_of_quadratic_equation(a, b, c):
    sp = []
    if a == 0 and b == 0 and c == 0:
        sp.append("all")
        return sp
    elif a == 0 and b == 0:
        return []
    elif c == 0:
        sp.append(0)
        sp.append(int(-b / a))
        return sp
    elif a == 0:
        sp.append(int(-c / b))
    else:
        d = b ** 2 - 4 * a * c
        if d > 0:
            sp.append(int((-b + sqrt(d)) / (2 * a)))
            sp.append(int((-b - sqrt(d)) / (2 * a)))
        elif d == 0:
            sp.append(int(-b / (2 * a)))
        else:
            return []
        return sp


result = roots_of_quadratic_equation(int(input('a = ')), int(input('b = ')), int(input('c = ')))
if 'all' in result:
    if result == ['all']:
        print('0 0 0')
    else:
        print('fail')
else:
    print(*sorted(result))
