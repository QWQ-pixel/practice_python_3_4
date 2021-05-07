def prime(number):
    if number == 1:
        return 'Не является ни простым, ни составным'
    else:
        k = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                k = k + 1
        if k <= 0:
            return 'Простое число'
        else:
            return 'Составное число'

