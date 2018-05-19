"""
Sort files based om extension.
"""

import os


def main():
    os.chdir('FilesToSort')

    # Go through all files
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            print(os.path.splitext(filename)[1])
            try:
                os.mkdir(os.path.splitext(filename)[1][1:])
                print('Folder does not exist')
            except FileExistsError:
                print('Folder exists')
            os.rename(filename, '{}/{}'.format(os.path.splitext(filename)[1][1:], filename))


main()
