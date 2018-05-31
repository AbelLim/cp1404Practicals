"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# 1. write down what you think the output of this will be,
# do_it(5) expected output is 3
# 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n <= 0:
        return 0
    print(n ** 2)
    do_something(n - 1)


# 3. write down what you think the output of do_something(4) will be,
# do_something(4) expected output RecursionError: maximum recursion depth exceeded
# 4. use the debugger to step through and see what's actually happening
do_something(4)

# 5. fix do_something() so that it works according to the docstring
