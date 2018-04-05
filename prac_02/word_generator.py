import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
word_format = ""
word = ""

# Allow user to define random word format.
user_word = str(input("Please type in a word: "))
user_word = user_word.lower()
for char in user_word.strip():
    if char in VOWELS:
        word_format += "v"

    elif char in CONSONANTS:
        word_format += "c"

# Generate random word based on word_format.
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)