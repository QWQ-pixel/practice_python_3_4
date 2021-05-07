def comment():
    words = ['import sys', 'for line in sys.stdin:',
             '# rstrip(’/n’) "отрезает" от строки line,',
             '# идущий справа символ перевода строки,',
             '# ведь print сам переводит строку',
             'print(line.rstrip(’/n’))']
    for word in list(filter(lambda x: '#' in x, words)):
        word = word.replace('#', '').strip()
        print('Line', str(words.index('# '+word)+1) + ':', word)


comment()
