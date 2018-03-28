"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
isNegative = False

while isNegative is False:
    sales = float(input("Enter Sales: $"))
    if sales < 0:
        isNegative = True
    elif sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15

    if isNegative is False:
        print("Your bonus is ${:.2f}".format(bonus))
    else:
        print("Invalid Input")
print()
