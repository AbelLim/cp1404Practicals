def main():
    """
CP1404/CP5632 - Practical
Broken program to determine score status
"""
    # Fix this!
    score = get_score()
    if score > 100:
        print("Invalid Score")
    elif score > 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score >= 0:
        print("Bad")
    else:
        print("Invalid Score")


def get_score():
    score = float(input("Enter score: "))
    return score


main()