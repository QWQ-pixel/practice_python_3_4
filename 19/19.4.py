def palindrome(s):
    if s == s[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'