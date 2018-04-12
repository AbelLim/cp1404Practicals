"""Counts the number of occurrences of each word in a user generated string."""


def main():
    # Get user input
    user_sentence = str(input("Please input a sentence: "))
    # Split string for each white space
    user_words = user_sentence.split()
    # Convert string to dictionary. Each value set to zero.
    word_occurrences = dict(zip(user_words, [0]*len(user_words)))

    # Check for each word in dictionary. Add 1 if found.
    for word in user_words:
        if word in word_occurrences:
            word_occurrences[word] = word_occurrences[word] + 1
        else:
            return

    print(word_occurrences)


main()
