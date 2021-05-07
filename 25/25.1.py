from random import sample
import string


def generate_password(m):
    symbols = string.ascii_letters + string.digits
    symbols = symbols.translate({ord(i): None for i in 'lI1oO0'})
    return ''.join(sample(symbols, m))


def main(n, m):
    return [generate_password(m) for _ in range(n)]


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
