# write a program that takes in a list of words as input and returns a new list that contains only words that has more than 6 or more characters.
words = ["Airline",	"Gigantic", "Publish", "Bandit", "Goofy", "Quadrangle",
         "Banquet", "Government"]


def words_filter(words):
    new_words = []
    for x in words:
        if len(x) > 6:
            new_words.append(x)
    return new_words


print(words_filter(words))
