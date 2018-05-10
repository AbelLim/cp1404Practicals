"""
Subclass of taxi. Has an additional attribute "fanciness" that scales the price_per_km value.
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name="Silver Service Taxi", fuel=0, fanciness=1):
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fanciness
        self.flagfall = 4.5

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

