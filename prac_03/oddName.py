"""Ask user for name and print every second letter."""


def main():
    user_name = get_name()
    frequency = get_frequency()
    print_name(user_name, frequency)


def print_name(user_name, frequency):
    # Print every character in user_name
    print("Showing every {} letter in your name.".format(frequency))
    for char in user_name[::frequency]:
        print(char)


def get_name():
    # Ask user for name.
    user_name = str(input("Please enter your name: "))
    # Check if user_name is blank.
    while len(user_name.strip()) == 0:
        user_name = str(input("Please enter your name: "))
    return user_name


def get_frequency():
    # Ask user for frequency.
    frequency = int(input("Please enter a number: "))

    # Check if frequency is a non-zero integer.
    while frequency == 0:
        frequency = int(input("Please enter a number: "))
    return frequency


main()
