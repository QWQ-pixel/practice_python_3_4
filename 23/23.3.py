def rhythm(msg):
    eq = [lett.count('а') for lett in msg.split()]
    return 'Парам пам-пам' if all(x == eq[0] for x in eq) else 'Пам парам'


# print(rhythm('пара-ра-рам рам-пам-папам па-ра-па-дам'))
