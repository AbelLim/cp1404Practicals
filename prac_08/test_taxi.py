"""
Test object from class Taxi
"""


def main():
    from prac_08.taxi import Taxi

    # Create a new taxi "Prius 1" with 100 units of fuel and a fare of $1.23 per km.
    prius = Taxi("Prius 1", 100)

    # Drive 40km.
    prius.drive(40)

    # Expected output: Prius 1, fuel=60, odometer=40, 40km on current fare, $1.23/km. The fare is $49.20.
    print("{}. The fare is ${:.2f}.".format(prius, prius.get_fare()))

    # Start a new fare and drive 100km.
    prius.start_fare()
    prius.drive(100)

    # Expected output: Prius 1, fuel=0, odometer=100, 60km on current fare, $1.23/km. The fare is $73.80.
    print("{}. The fare is ${:.2f}.".format(prius, prius.get_fare()))


main()

