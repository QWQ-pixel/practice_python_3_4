def ask_password():
    string = 'password'
    count = 3
    while count != 0:
        str = input()
        if str == string:
            print('Пароль принят')
        if str != string and count == 0:
            print('В доступе отказано')
        count -= 1
