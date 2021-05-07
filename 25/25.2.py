from random import sample
import string


def generate_password(m):
    symbols = string.ascii_letters + string.digits
    symbols = symbols.translate({ord(i): None for i in 'lI1oO0'})
    letters = string.ascii_uppercase.translate({ord(i): None for i in 'IO'})
    numbers = string.digits.translate({ord(i): None for i in '10'})
    password = ''.join(sample(symbols, m))
    if len(set(numbers).intersection(set(password))) > 0 and len(set(letters).intersection(set(password))) > 0:
        return password
    else:
        generate_password(m)


def main(n, m):
    return [generate_password(m) for _ in range(n)]


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
