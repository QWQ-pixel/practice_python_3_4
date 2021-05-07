def translate(text):
    letters = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я', ',', '.', '-', '!', '?']
    for let in text:
        if let.lower() in letters and len(let) == 1:
            text = text.replace(let, '')
    return text.split()


