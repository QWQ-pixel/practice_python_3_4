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


def solve(coefficients):
    if len(coefficients.split()) > 3 or coefficients is None:
        return None
    else:
        return roots_of_quadratic_equation(int(coefficients.split()[0]), int(coefficients.split()[1]), int(coefficients.split()[2]))


print(*sorted(solve(input())))
