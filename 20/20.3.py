list_of_jokes = []


def print_only_new(joke):
    if joke not in list_of_jokes:
        list_of_jokes.append(joke)
        print(joke)

