"""
Allow user to add guitar to list of guitars. Allow the user to view the list of guitars.
"""

from prac_07.guitar import Guitar


def main():
    print("My Guitars!")
    guitars = []
    is_blank = False

    while is_blank is False:
        guitar_name = input("Name: ")
        if guitar_name is "":
            is_blank = True
        else:
            guitar_year = int(input("Year: "))
            guitar_cost = float(input("Cost: "))
            new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
            guitars.append(new_guitar)
            print("{} added.".format(new_guitar))
    """
    Sample values
    """
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Another Guitar", 2012, 230.99))

    for index, guitar in enumerate(guitars):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {} ({}), worth $ {:.2f} {}"
              .format(index+1, guitar.name, guitar.year, guitar.cost, vintage_string,))


main()
