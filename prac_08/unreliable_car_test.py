"""
Test object from UnreliableCar
"""


def main():
    from prac_08.unreliable_car import UnreliableCar

    used_car = UnreliableCar("Used Car", 100, 50)
    used_car.drive(40)
    print(used_car)


main()
