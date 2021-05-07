def gematria():
    words = []
    b, count = ord('A'), 0
    while True:
        string = input()
        if string == '':
            break
        words.insert(count, string)
        count += 1
    return sorted(words, key=lambda word: sum([(ord(i) - ord('A') + 1) for i in word.upper()]))


# print(*gematria(), sep='\n')
