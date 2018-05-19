"""
Sort files based on user input.
"""

import os


def main():
    os.chdir('FilesToSort')

    # Go through all files
    extensions = []
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            try:
                if format(os.path.splitext(filename)[1]) not in extensions:
                    directory = str(input('What category would you like to sort {} files into? '.format(os.path.splitext(filename)[1][1:])))
                    os.mkdir(os.path.splitext(directory)[1])
            except FileExistsError:
                pass
            finally:
                os.rename(filename, '{}/{}'.format(os.path.splitext(filename)[1][1:], filename))


main()
