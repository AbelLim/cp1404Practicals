"""
A shop requires a small program that would allow them to quickly work out total price for a number of items,
each with different prices.
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the
screen.

"""
# Initialize values
totalPrice = 0

# Allow user to enter the number of items
numberOfItems = int(input("Number of items: "))
while numberOfItems <= 0:
    print("Invalid number of items!")
    numberOfItems = int(input("Number of items: "))

# Allow user to enter price of each item
for i in range(numberOfItems):
    itemPrice = float(input("Price of item: $"))
    totalPrice = totalPrice + itemPrice

# Apply discount if the total price is more than $100
if totalPrice > 100:
    totalPrice = totalPrice * 0.9

# Display total price to the user
print("Total price for {} items is ${:.2f}".format(numberOfItems, totalPrice))