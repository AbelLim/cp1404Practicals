"""
Subclass of car. Has an additional attribute "reliability" which represents the chance of the car to drive.
"""

from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name="car", fuel=0, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, reliability {}%".format(super().__str__(), self.reliability)

    def drive(self, distance):
        reliability_check = random.randint(0, 100)
        if reliability_check < self.reliability:
            return super().drive(distance)
        else:
            return 0

