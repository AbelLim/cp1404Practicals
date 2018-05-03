"""
Class containing information about object Guitar
"""
import datetime
now = datetime.datetime.now()


class Guitar:
    def __init__(self, name, year, cost):
        """Define attributes of Guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Define identifying string of Guitar"""
        return "{}({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = now.year - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False

