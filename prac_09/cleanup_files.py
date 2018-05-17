"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo of os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    """
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    """

    # Loop through each file in the (current) directory
    """
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        """

    # Try these options one at a time
    # Option 1:  rename file to new name - in place
    # os.rename(filename, new_name)

    # Option 2: move file to new place, with new name
    # shutil.move(filename, 'temp/' + new_name)

    # Process all subdirectories using os.walk()
    os.chdir('..')  # '..' means to go 'up' one directory
    lyrics_path = os.getcwd()  # store the path so we can get back to it
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})\n".format(os.getcwd()))

        # Change into the directory and print the current working directory
        os.chdir(directory_name)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in os.listdir('.'):
            # Ignore directories, just process files
            if os.path.isdir(filename):
                pass
            else:
                new_name = get_fixed_filename(filename)
                print("Renaming {} to {}".format(filename, new_name))

        # then change back to the lyrics_path
        os.chdir(lyrics_path)
        print("(Current working directory is: {})\n".format(os.getcwd()))

        # Note: if you get this wrong, walk will stop short,
        # so you need to check it still walks through all subdirectories
        # add a loop (in between directory changes) to rename the files


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_word = ""
    last_char = ""
    new_name = filename.replace(" ", "_")

    for char in new_name:
        if char.isupper():
            if last_char == "" or last_char == "_":
                last_char = char
            else:
                last_char = char
                char = "_{}".format(char)
        elif char == "_":
            last_char = char
        elif char.isnumeric():
            if last_char.isnumeric() or last_char == "_":
                last_char = char
            else:
                last_char = char
                char = "_{}".format(char)

        new_word = new_word + char

    new_name = new_word
    new_name = new_name.title()
    new_name = new_name.replace(".T_X_T", ".txt").replace("._T_X_T", ".txt").replace(".Txt", ".txt")

    return new_name


main()
