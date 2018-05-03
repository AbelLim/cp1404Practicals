"""
Class for object Programming Language. It contains information about characteristics of the language.
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialize ProgrammingLanguage object. Define attributes belonging to this language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Define string for object Programming Language"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        return self.typing
