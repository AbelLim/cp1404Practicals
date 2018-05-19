"""
Sort files based on user input.
"""

import os


def main():
    os.chdir('FilesToSort')

    # Go through all files
    # Create relationships between files and subdirectories
    relations = {}
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            try:
                relations[os.path.splitext(filename)[1][1:]]
            except KeyError:
                directory = str(input(
                    'What category would you like to sort {} files into? '.format(os.path.splitext(filename)[1][1:])))
                try:
                    os.mkdir(directory)
                except FileExistsError:
                    pass
                relations[os.path.splitext(filename)[1][1:]] = directory
            os.rename(filename, '{}/{}'.format(relations[os.path.splitext(filename)[1][1:]], filename))


main()
