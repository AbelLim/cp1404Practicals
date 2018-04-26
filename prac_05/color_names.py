"""Take in name of color from user and output the hexadecimal code for the color."""

# Define dictionary of COLOR_CODES as a constant.
COLOR_CODES = {"AliceBlue": "#f0f8ff", "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2", "CadetBlue": "#5f9ea0",
               "CornflowerBlue": "#6495ed", "DarkGoldenrod": "	#b8860b", "DarkGreen": "#006400", "DarkKhaki": "#bdb76b",
               "DarkOrange": "#ff8c00", "DarkOrchid": "#9932cc"}


def main():

    user_input = input("Please input a color name: ")

    if user_input in COLOR_CODES:
        print("The color code for {} is {}".format(user_input, COLOR_CODES[user_input]))
    else:
        print("Invalid color code.")


main()
