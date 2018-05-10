"""
Test object for SilverServiceTaxi
"""


def main():
    from prac_08.silver_service_taxi import SilverServiceTaxi

    hummer = SilverServiceTaxi("Hummer", 200, 4)
    hummer.drive(18)
    print("${:.2f}".format(hummer.get_fare()))


main()