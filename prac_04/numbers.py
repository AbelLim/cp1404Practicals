"""Take in five user defined numbers and outputs various information about the numbers."""

# Contains the main section of code.
def main():
    numbers = list()

    # Get five user inputs and store them in numbers.
    while len(numbers) < 5:
        numbers.append(get_input())

    print_numbers(numbers)


def print_numbers(numbers):
    # Print information about the list
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))


# Request integer user input.
def get_input():
    user_input = int(input("Number: "))
    return user_input


main()
