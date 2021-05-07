import calendar


def month_name(num, lang):
    month = calendar.month_name[num]
    ru = {'January': 'Январь', 'February': 'Феврать',
          'March': 'Март', 'April': 'Апрель',
          'May': 'Май', 'June': 'Июнь',
          'July': 'Июль', 'August': 'Август',
          'September': 'Сентябрь', 'October': 'Октябрь',
          'November': 'Ноябрь', 'December': 'Декабрь'}
    if lang == 'ru':
        print(ru[month])
    else:
        print(month)