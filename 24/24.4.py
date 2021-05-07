words = sorted([input().lower() for _ in range(int(input()))])
anagram = {}


def sorted_string(s):
    return ''.join(sorted(s))


def anagrams():
    for word in words:
        sorted_word = sorted_string(word)
        anagram.setdefault(sorted_word, [])
        anagram[sorted_word].append(word)

    for w, a in anagram.items():
        if len(set(a)) > 1:
            print(*sorted(set(a)))


anagrams()
