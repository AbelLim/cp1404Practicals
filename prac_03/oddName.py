"""Ask user for name and print every second letter."""


def main():
    # Ask user for name.
    user_name = str(input("Please enter your name: "))

    # Check if user_name is blank.
    while len(user_name.strip()) == 0:
        user_name = str(input("Please enter your name: "))

    # Print every character in user_name
    print("Showing every odd letter in your name.")
    for char in user_name[::2]:
        print(char)

main()