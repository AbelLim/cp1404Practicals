"""
Test program for methods in object Guitar
"""

from prac_07.guitar import Guitar


def main():
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Another Guitar", 2012, 230.99)

    print(guitar_1)
    print(guitar_2)

    print("{} get_age. Expected 96 Got {}".format(guitar_1.name, guitar_1.get_age()))
    print("{} get_age. Expected 6 Got {}".format(guitar_2.name, guitar_2.get_age()))

    print("{} is_vintage. Expected True Got {}".format(guitar_1.name, guitar_1.is_vintage()))
    print("{} is_vintage. Expected False Got {}".format(guitar_2.name, guitar_2.is_vintage()))


main()
