def print_upper_words(words, starts_with):
    """takes a list of words and returns each word in uppercase on a new line"""


    i = 0
    while i < len(starts_with):
        starts_with[i] = starts_with[i].upper()
        i += 1

    for word in words:
        uppercased = word.upper()
        if uppercased[0] in starts_with:
            print(uppercased)

print_upper_words(["hello", "HI", "TeSt", "Electric", "elephant"], starts_with=["e", "H"])