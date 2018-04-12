"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ")
while state != "":
    if state.upper() in str(STATE_NAMES):
        print(state, "is", STATE_NAMES[state.upper()])
    elif state.upper() == "ALL":
        for key in STATE_NAMES:
            print("{:<3} is {}".format(key, STATE_NAMES[key]))
    else:
        print("Invalid short state")
    state = input("Enter short state: ")
