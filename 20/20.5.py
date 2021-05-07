def lucky(ticket):
    if len(str(ticket)) < 6:
        ticket = str(ticket).zfill(6)
    if sum([int(char) for char in str(ticket)[:3]]) == sum([int(char) for char in str(ticket)[3:]]):
        if sum([int(char) for char in str(lastTicket)[:3]]) == sum([int(char) for char in str(lastTicket)[3:]]):
            return 'Счастливый'
        else:
            return 'Несчастливый'
    else:
        return 'Несчастливый'


