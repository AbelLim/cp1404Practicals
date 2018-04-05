"""
Generate a user-defined number of rows with 6 columns of numbers. These numbers should not contain any repetitions and
should be sorted in ascending order.
"""


def main():
    COLUMN = 6
    row = get_row()
    quick_picks = list()

    print("{} , {}".format(COLUMN, row))

    # Generate a number of rows equal to the number defined by the user.
    x = 0
    while x < row:
        print(generate_row(COLUMN))
        x = x + 1


# Request user input for the number of rows.
def get_row():
    row = int(input("How many quick picks do you wish to generate?: "))
    return row

# Generate random numbers (from 1 to 45) equal to the number of columns into a list
def generate_row(column):
    import random

    RANDOM_MIN = 1
    RANDOM_MAX = 45

    numbers = list()
    x = 0
    while x < column:
        new_number = random.randint(RANDOM_MIN, RANDOM_MAX)
        numbers.append(new_number)
        x = x + 1

# Sort generated numbers in list
    numbers.sort()
    return numbers


main()
