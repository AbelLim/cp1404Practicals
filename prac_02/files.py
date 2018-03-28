"""
1. Write a program that asks the user for their name, then opens a file called “name.txt” and writes that
name to it.
2. Write a program that opens “name.txt” and reads the name (as above) then prints,
“Your name is Bob” (or whatever the name is in the file).
3. Create a text file called “numbers.txt” (You can create a simple text file in PyCharm with Ctrl+N, choose
“File” and save it in your project). Put the numbers 17 and 42 on separate lines in the file and save it:
17
42
Write a program that opens “numbers.txt”, reads the numbers and adds them together then prints the
result, which should be… 59.
"""

out_file = open("name.txt", "w")
user_name = str(input("Please enter your name: "))
print(user_name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
user_name = in_file.read()
print("Your name is {}".format(user_name))
in_file.close()

total_sum = 0
in_file = open("numbers.txt", "r")
for line_str in in_file:
    total_sum = total_sum + int(line_str)
print("The total sum is {}".format(total_sum))
