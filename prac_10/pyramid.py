"""
Calculate the total number of blocks in a pyramid structure with n rows
"""


def calculate_total(rows):
    if rows <= 0:
        return 0
    return rows + calculate_total(rows - 1)


print(calculate_total(5))
