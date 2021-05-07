from random import sample
import string


def check(num, up_l, low_l, pwd):
    if len(num.intersection(set(pwd))) > 0 and len(up_l.intersection(set(pwd))) > 0 and len(
            low_l.intersection(set(pwd))) > 0:
        return True
    else:
        return False


def generate_password(m):
    letters_upper = set(string.ascii_uppercase.translate({ord(i): None for i in 'IO'}))
    numbers = set(string.digits.translate({ord(i): None for i in '10'}))
    letters_lower = set(string.ascii_uppercase.translate({ord(i): None for i in 'lo'}))
    symbols = string.ascii_letters + string.digits
    symbols = symbols.translate({ord(i): None for i in 'lI1oO0'})
    password = ''.join(sample(symbols, m))
    if check(numbers, letters_upper, letters_lower, password):
        return password
    else:
        return generate_password(m)


def main(n, m):
    return [generate_password(m) for _ in range(n)]


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
