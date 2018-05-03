"""
Defining languages from object Programming Language
"""

from prac_07.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    languages = [ruby, python, visual_basic]
    dynamic_languages = []
    for language in languages:
        if language.typing == "Dynamic":
            dynamic_languages.append(language.name)

    print("The dynamically typed languages are:")
    for language in dynamic_languages:
        print(language)


main()
