"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month = int(input("How many months? "))

    for x in range(1, month + 1):
        income = float(input("Enter income for month {:2}: ".format(str(x))))
        incomes.append(income)

    print_report(incomes, month)


def print_report(incomes, month):
    print("\nIncome Report\n-------------")
    total = 0
    for x in range(1, month + 1):
        income = incomes[x - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(x, income, total))


main()
