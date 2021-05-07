sights = [' ', '!', '?', '-', '.']


def encrypt_caesar(msg_, shift_=3):
    encrypt_msg = ''
    for let in msg_:
        if let in sights:
            encrypt_msg += let
        else:
            encrypt_msg += chr(ord(let) + shift_)
    return encrypt_msg


def decrypt_caesar(msg_, shift_):
    return encrypt_caesar(msg_, -shift_)


msg = "Да здравствует салат Цезарь!"
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
# print(encrypted)
# print(decrypted)
