"""
Generate a user-defined number of rows with 6 columns of numbers. These numbers should not contain any repetitions and
should be sorted in ascending order.
"""


def main():
    COLUMN = 6
    row = get_row()
    lottery_tickets = list()

    print("{} , {}".format(COLUMN, row))

    # Generate a number of rows equal to the number defined by the user.
    x = 0
    while x < row:
        lottery_tickets.append(generate_row(COLUMN))
        x = x + 1
    print(lottery_tickets)


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
    number = 0
    new_number = 0
    while number < column:
        # Check for repeated numbers and regenerating if the generated number is already present.
        is_repeated = True
        while is_repeated is True:
            new_number = random.randint(RANDOM_MIN, RANDOM_MAX)
            if new_number in numbers:
                is_repeated = True
            else:
                is_repeated = False
        numbers.append(new_number)
        number = number + 1

# Sort generated numbers in list
    numbers.sort()
    return numbers


main()
