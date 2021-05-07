def do_bet(horse, money):
    if horse < 10 and horse not in horses and money > 0:
        print('Ваша ставка в размере', money, 'на лошадь', horse, 'принята')
        horses.append(horse)
    else:
        print('Что-то пошло не так, попробуйте еще раз')


horses = []
