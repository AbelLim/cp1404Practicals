"""
Generate a user-defined number of rows with 6 columns of numbers. These numbers should not contain any repetitions and
should be sorted in ascending order.
"""


def main():
    import random

    COLUMN = 6
    row = get_row()

    print("{} , {}".format(COLUMN, row))


def get_row():
    row = int(input("How many quick picks do you wish to generate?: "))
    return row


main()
