"""Counts the number of occurrences of each word in a user generated string."""


def main():
    user_sentence = str(input("Please input a sentence: "))
    word_occurrences = dict(zip(user_sentence.split(), [0]*len(user_sentence)))
    print(word_occurrences)


main()
