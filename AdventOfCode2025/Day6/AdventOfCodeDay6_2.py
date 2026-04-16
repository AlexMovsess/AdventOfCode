import os
import re
import math

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay6.txt")) as f:
    content = f.read()
    lines = content.split("\n")
    matrix = [re.split("", line) for line in lines]

# Simple formatting due to regex adding '' at beginning and end of line
for line in matrix:
    line.pop(-1)
    line.pop(0)

number_list = []
total = 0

# Read right to left
for i in range(len(matrix[0]) - 1, -1, -1):

    number = matrix[0][i] + matrix[1][i] + matrix[2][i] + matrix[3][i]

    # Ignore empty lines
    if (
        matrix[0][i] != " "
        or matrix[1][i] != " "
        or matrix[2][i] != " "
        or matrix[3][i] != " "
    ):

        number = int(number.strip())
        number_list.append(number)

        if matrix[4][i] == "+":
            total += sum(number_list)
            number_list = []

        elif matrix[4][i] == "*":
            total += math.prod(number_list)
            number_list = []

print(total)
