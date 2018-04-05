"""Check username against a list of authorised usernames."""


def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
                 'InterpreterInterface', 'StartServer', 'bob']

    username = get_username()

    # Check if username matches the list of authorised usernames.
    if username in usernames:
        print("Access Granted")

    else:
        print("Access Denied")


# Get username from user.
def get_username():
    username = str(input("Please enter your username: "))
    return username


main()
