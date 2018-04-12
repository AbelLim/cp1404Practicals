"""Take in name of color from user and output the hexadecimal code for the color,"""

# Define dictionary of COLOR_CODES as a constant.
COLOR_CODES = {"AliceBlue": "#0F0F88F"}


def main():
    user_input = input("Please input a color name: ")

    if user_input in COLOR_CODES:
        print("The color code for {} is {}".format(user_input, COLOR_CODES[user_input]))
    else:
        print("Invalid color code.")


main()
