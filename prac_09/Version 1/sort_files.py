"""
Sort files based on extension.
"""

import os


def main():
    os.chdir('FilesToSort')

    # Go through all files
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            try:
                os.mkdir(os.path.splitext(filename)[1][1:])
            except FileExistsError:
                pass
            os.rename(filename, '{}/{}'.format(os.path.splitext(filename)[1][1:], filename))


main()
